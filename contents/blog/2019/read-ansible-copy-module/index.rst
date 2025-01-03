===========================================================
Ansibleのcopyモジュールはどうやって冪等性を担保しているのか
===========================================================

.. post:: 2019-12-09
   :category: Tech
   :tags: Python,Ansible,

.. note::

   この記事は、Qiitaの `Ansible Advent Calendar 2019 <https://qiita.com/advent-calendar/2019/ansible>`_ の 9日目の記事です。[#]_

前書き
======

今年の `PyCon JP <https://pycon.jp/2019/>`_ で
`「Ansibleを通じて「べき等性」を理解してみよう」 <https://pycon.jp/2019/sessions?sessionId=221>`_
というトークをしました。

* `HTML版 <https://slides.attakei.net/pyconjp-2019>`_
* `PDF版 <https://speakerdeck.com/attakei/try-understanding-idempotency-by-ansible>`_

このトークではAnsibeの冪等性担保のアプローチを ``yum`` モジュールで理解したのですが、

**「何であろうと ``yum`` コマンドを実行して、出力結果とリターンコードで判断する」**

というものでした。

このときもらった質問+やり取りで、

* Q: サーバー内でのファイルコピーとかどうしてるんでしょう？(意訳)
* A: ローカルでファイルを保持して、 ``copy`` モジュールとか使います(意訳)

というのがありました。

そこで今回はAdventCalendarに乗じて、
「 ``yum`` ではああだったが、 ``copy`` ではどうだろう？ 」
というのを検証しようと思います。

copyとyumを見比べる
===================

ソースを読んで見る前に、ちょっと挙動をおさらいしてみます。

================== ================================= ================================
 項目               yum                               copy
================== ================================= ================================
| 何をするか       | yumコマンドを操作する           | ローカルからファイルを転送する
| Changed条件      | パッケージの有無に変化があった  | ファイルの有無に変化があった
                   | or                              | or
                   | パッケージを更新した            | ファイルを更新した
| やってそうなこと | * インストール状態の把握        | * 何かしらでファイルの新旧比較
                   | * 必要に応じてyumコマンドの実行 | * 必要に応じてファイルの転送
================== ================================= ================================

※ ``yum`` については、文字通りPyCon発表以前に想像した「やっそうなこと」で、
実際の動作は前述のスライドのとおりです。

気になるのは ``copy`` モジュールの場合このあたりの動作はどう変わってくるか。

``yum`` と同じく「とりあえずファイルを転送」というのは考えづらいです。
というのも、

* ``stat`` コマンドを使っても、ファイルサイズまでしかわからない
* ``cp`` コマンドの挙動的に、

  * inodeは変化しない
  * ファイルの内容にかかわらずChangedは変化する
  * ファイルの内容変化はわからない
* ``copy`` モジュールには ``backup`` パラメーターが存在する

となるため、「なにかしらの判定を挟まないと、OK/Changedが判定できない」と考えられそうです。

.. literalinclude:: ./stat-command.txt

実際に調べてみる
================

というわけで、ここからはコードリーディングタイムです。
なお、今回はリリースしたばかりの ``v2.9.2`` で挙動を確認してみます。 [#]_ [#]_


まずはmain()から
----------------

Ansibleモジュールの比較的基本となる原則として、
「 ``main()`` を定義して、 ``__name__ == '__main__'`` で呼ぶ、実行向けの構成を取る」
というのがあります。今回もそれに当てはまるので、まずは ``main()`` 関数を眺めてみます。

チェックサムを調べている
------------------------

.. literalinclude:: ./ansible-copy-module.py
    :language: python
    :lines: 550-564
    :linenos:
    :lineno-start: 550

`引数の下処理の少し後 <https://github.com/ansible/ansible/blob/v2.9.2/lib/ansible/modules/files/copy.py#L552>`_ に、
転送予定ファイルのチェックサムを取得して ``checksum_src`` に保存しいるところがあります。
すごくそれっぽいですね。

.. literalinclude:: ./ansible-copy-module.py
    :language: python
    :lines: 604-611
    :linenos:
    :lineno-start: 604

`更に読み進めると <https://github.com/ansible/ansible/blob/v2.9.2/lib/ansible/modules/files/copy.py#L604>`_ 、
転送先予定のパスにすでにファイルがある場合に、そのファイルのチェックサムを ``checksum_dest`` に保存しています。
だんだん答えが見えてきました。

チェックサムを比較している
--------------------------

.. code-block:: python

    if checksum_src != checksum_dest or os.path.islink(b_dest):
        if not module.check_mode:
            # 状況に応じた様々な処理
            try:
                if backup:
                    pass
            except (IOError, OSError):
                module.fail_json(msg="failed to copy: %s to %s" % (src, dest), traceback=traceback.format_exc())
        changed = True
    else:
        changed = False

`終盤に入ると <https://github.com/ansible/ansible/blob/v2.9.2/lib/ansible/modules/files/copy.py#L629>`_ 、
``checksum_dest`` と ``checksum_src`` の状況に応じて、条件分岐するようになっています。
上記の抜粋ではかなり省略してますが、重要なのは ``else`` の方で、
この記述を持って
「両者のチェックサムが一致した場合は、変更を加えずに ``changed = False`` とする」
実装となっているのが見て取れます。

フォルダごとの転送でも頑張る
----------------------------

チェックサムの確認は、いずれも ``os.path.isfile`` が ``True`` のときのみ行われます。
``src``, ``dest`` どちらもがフォルダの場合は結果が ``None`` になるので、上記の転送処理に入りません。[#]_

ただし、 ``remote_src=yes`` の場合に限り、後続処理が定義されています。[#]_
この場合は、 ``copy_diff_files()`` 関数を用いて内部で、ファイルのdiffを取って判定しています。

.. literalinclude:: ./ansible-copy-module.py
    :language: python
    :lines: 399-409
    :linenos:
    :lineno-start: 399

`関数内にて <https://github.com/ansible/ansible/blob/v2.9.2/lib/ansible/modules/files/copy.py#L399>`_
``filecmp.dircmp(src, dest).diff_files`` が実行されて、差分が存在するファイルをリスト化を行います。
そして1ファイルでも存在すれば ``changed = True`` となるように実装されてます。
もちろん差分がなければ ``changed = False`` で何もしません。

結論
====

``copy`` モジュールは、

* ローカルtoリモートでのファイルコピー時には、``sha1`` でのチェックサムを比較して上書き要否を判定する
* リモート上でのファイルコピー時には、 ``filecmp`` モジュールを利用して上書き要否を判定する

という挙動を取って冪等性を担保しているようでした。
まぁ ``yum`` モジュールよりは混みいった実装をしないと難しいようです。

余談
----

ちなみに、複雑度計測ツールの ``lizard`` で2個のモジュールを比較してみると、

.. literalinclude:: ./lizard-result.txt

こんな感じになります。意外なことに ``copy`` モジュールのほうが少ない行数で記述されているようです。

* 意外なことに、 ``copy`` のほうが少ない行数となっている。
* CNN(複雑度)は、 ``copy`` のほうが高い。
* ``yum`` は処理を細かく散らしているに対して、 ``copy`` は少数に加えて ``main`` がやばめ。

といった違いがあります。
用途や原作によってモジュールもずいぶん違うのだなという感想で、
この記事は終了とさせていただきます。

.. [#] 普段はQiitaで書きそうな記事ですが、ちょっと思いつきで自分のブログ行きになりました。
.. [#] https://github.com/ansible/ansible/blob/v2.9.2/lib/ansible/modules/files/copy.py
.. [#] 2.9で若干修正が入っていますが、そこまで大きなな修正ではないものとします。
.. [#] デフォルトでは ``no`` となってます
.. [#] ``None != None`` は ``False``
