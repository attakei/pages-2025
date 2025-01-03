==============================================
AnsibleモジュールのテストをPy.testで書いてみる
==============================================

.. post:: 2019-05-24
   :category: Tech
   :tags: python, ansible, pytest,

ちょっと野良Ansibleモジュールを作る感じになったので、
「せっかくだからある程度テストコードも書いてみよう」と思い、
あれこれ試行錯誤している最中のメモ。

前提
====

* ローカルモジュールとして動かすことを前提にしたコードを書く
* https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html#developing-modules-general がベース

  * モジュール全体のテストは、 **"Exercising module code locally"** セクションを真似に行く

* https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/basic.py この辺を読みつつ解決してる

課題1: AnsibleModuleのexit_json,fail_jsonがSystemExitを返すのでテストが死ぬ
===========================================================================

内容
----

Ansibleモジュールを定義するときには、最終的に ``AnsibleModule`` オブジェクトを用意して、

* パラメーターの読み込みとチェック
* 正否の結果をAnsibleに通知

を行うことになっている。

で、後者の「正否判定の通知」は ``exit_json`` , ``fail_json`` を使って結果を伝えているのだが、
Ansibleの挙動上、リモート先でのモジュールは1個のコマンドとして実行され、
どちらのコマンドも最後は ``sys.exit`` が呼ばれて終了する。

py.testでモジュール実行自体をテストしようとすると、何度も呼び出す必要が出てくるのだが、
``sys.exit`` だ途中に入るため、テストが回らずに死んでしまう。

対策
----

.. code-block:: python

    import pytest
    import local_module  # テスト対象のモジュール。ちゃんと処理内で、パラメーターのチェックをする

    def test_no_args():
        """何もパラメーターが無いと、リターンコード1が返る
        """
        with pytest.raises(SystemExit) as exited:
            local_module.main()
        assert exited.value.code == 1

`sys.exit()` が ``SystemExit`` を送信するので、これをwithコンテキストでキャッチして、
中身を検証する構成を基本としてみている。

課題2: テスト中にパラメーター読み込みで結果が変わらず、テストが機能しない
=========================================================================

このテストが全てパスしてくれず、どちらかがNGになる模様。

.. code-block:: python

    import io
    import json
    import pytest
    import local_module  # テスト対象のモジュール。ちゃんと処理内で、パラメーターのチェックをする

    def test_no_args():
        """何もパラメーターが無いと、リターンコード1が返る
        """
        with pytest.raises(SystemExit) as exited:
            local_module.main()
        assert exited.value.code == 1

    def test_with_args(monkeypatch):
        """nameパラメーターがあれば、リターンコード0が返る
        """
        with pytest.raises(SystemExit) as exited:
            stdin = json.dumps({'ANSIBLE_MODULE_ARGS': {'name': 'hello'}})
            monkeypatch('sys.stdin', io.String(stdin))
            local_module.main()
        assert exited.value.code == 0

なにもカスタマイズせずに ``AnsibleModule`` を呼び出すと、
内部で ``_load_params`` というパラメーター読み取り用の関数が呼ばれる。
これがモジュール内変数 ``_ANSIBLE_ARGS`` を ``global`` 宣言してキャッシュに使っており、
ユニットテストなどで、複数回 ``_load_params`` を呼んでも最初の1回分しか使用されないらしい。

対策
----

``_ANSIBLE_ARGS`` にもmonkeypatchを当てる。以上

.. code-block:: python

    import io
    import json
    import pytest
    import local_module  # テスト対象のモジュール。ちゃんと処理内で、パラメーターのチェックをする

    def test_no_args(monkeypatch):
        """何もパラメーターが無いと、リターンコード1が返る
        """
        monkeypatch('sys.stdin', None)
        with pytest.raises(SystemExit) as exited:
            local_module.main()
        assert exited.value.code == 1

    def test_with_args(monkeypatch):
        """nameパラメーターがあれば、リターンコード0が返る
        """
        monkeypatch('sys.stdin', None)
        with pytest.raises(SystemExit) as exited:
            stdin = json.dumps({'ANSIBLE_MODULE_ARGS': {'name': 'hello'}})
            monkeypatch('sys.stdin', io.String(stdin))
            local_module.main()
