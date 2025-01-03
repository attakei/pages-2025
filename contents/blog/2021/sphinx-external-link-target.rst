=========================================
サイトの外部リンクを別窓にする for Sphinx
=========================================

.. post:: 2021-09-07
   :category: Tech
   :tags: Python,Sphinx,

ちょっとSphinx用の拡張コードを書いて、
サイト内にある外部サイト [#]_ へのリンクを別タブ（別窓）で開くようにしました。
今のところは、ライブラリとしての公開は一拍置く予定で、実装の考え方をメモがてら書き置きします。

Sphinx(rST)におけるリンクの考え方
=================================

Sphinxでのリンクの書き方はいくつかありますが、
このあたりの内容自体は
`Sphinx日本ユーザー会のサイト <https://sphinx-users.jp/reverse-dict/writing/link.html>`_
を参照してもらったほうが早いので割愛します。

それぞれの書き方をすると、リンク先・リンク内テキスト・その他要素などのパースを行い、
``reference`` というノードに変換します。
この参照ノードを元に、後述ビルダー達は各種出力を行います。

SphinxのHTMLビルドにおいて、リンク=a要素はどのように生成されるか
================================================================

Sphinxでアウトプットをどのようにするかは、主にビルダーの担当となっています。
雑に書くと、HTMLを生成するためには、このような流れになっています。

#. ``html`` ビルドを用いて ``StandaloneHTMLBuilder`` によるビルドを実行
#. ビルダーは出力のための各種準備を行い、 ``HTML5Translator`` というライターに出力を委譲

``HTML5Translator`` には、ノードごとに
``visit_xxxx`` , ``depart_xxxx`` といったメソッドが定義されており、
文字通り、ノードの開始/終了時に随時呼び出される形式になっています。

今回のリンクなどは前述の通り ``reference`` ノードです。
`HTML5Translatorのコード <https://github.com/sphinx-doc/sphinx/blob/4.x/sphinx/writers/html5.py#L212>`_
には ``visit_reference`` というメソッドが確認でき、
ここで ``a`` 要素を生成していることが分かります。

処理を継ぎ足して、無理矢理外部リンク化する
==========================================

現在では、外部リンクを別窓などで開くための ``a`` 要素には、
``target="_blank"``  だけでなく ``rel="noreferer"`` を指定することが多いです。
しかし、 ``HTML5Translator.visit_reference`` の実装には、 ``rel`` 属性の入り込む余地がありません。 [#]_

そのため、「まるごと実装を差し替える」「一度出力して置換する」などの強硬策で別窓化する必要があります。
今回は「まるごと実装を差し替える」形式で実現しています。

.. code-block:: python

    def visit_reference(self, node):
        atts = {"class": "reference"}
        if node.get('internal') or 'refuri' not in node:
            atts['class'] += ' internal'
        else:
            atts['class'] += ' external'
            # overwritten
            atts['target'] = '_blank'
            atts["rel"] = "noreferrer"

もともとの ``HTML5Translator.visit_reference`` が定義している実装をまるまるコピペしています。
その上で、内部リンクor外部リンクの判定をしているブロックを見つけ、
外部リンクだった際に属性2個を追加しています。

.. code-block:: python

    from sphinx.writers.html5 import HTML5Translator

    # 中略

    def setup(app):
        app.add_node(
            reference, True, html=(visit_reference, HTML5Translator.depart_reference)
        )

``reference`` ノードに対する開始/終了の処理ペアを、
開始のみ実装したものに上書きします。

これで、外部リンク判定のものに対してはHTML生成時に ``target="_blank"`` 等が付与されるようになります。

ライブラリ化を躊躇している理由
==============================

それなりに便利な実装なのですが、現状だとプライベートPyPI含めてパッケージ化していません。

このあたりの理由は大きく3つあります。

* テスト・構造を一切度外視して結果のみを優先したので、想定外のケースへの対処を何もしていない
* もうちょっとマシな実装がありそう(コードのコピペ実装すぎるので、堅牢性がなさすぎる)
* 優先順位が低い

「マシな実装」が思い浮かびそうなら、冬以降に考えてみます。

.. [#] 「自サイトのドメイン以外」ではなく「Sphinxのrstパース時に ``external`` 判定したもの」としています、楽なので。
.. [#] ``attrs`` で属性を取りまとめているのですが、引数で渡ってくる ``node`` から細かく属性をピックアップするようにななっていません。
