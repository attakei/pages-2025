===============================================================
Windows版VisualStudioCodeで、スムーズvenvを使うための設定まとめ
===============================================================

.. post:: 2019-07-27
   :category: Tech
   :tags: Python,VisualStudioCode,Windows,

今月から使っているOneMix3SはもうしばらくWindowsのままでいく予定のため、
VSCodeなどの設定を整理している。

環境情報
========

* Windows 10 Home
* Visual Studio Code 1.36.1
* Python 3.7.4

1. venvを作成する
=================

起動時点で統合ターミナルは、PowerShellとして起動するので、 ``venv`` の作成自体は簡単。
今回は、プロジェクト内に ``.venv`` フォルダに用意する方向で進める。

.. code-block:: shell

   $ py -m venv .venv

``settings.json`` に ``venv`` 内にあるPythonを指定すると、
次回以降にターミナルを起動するときに自動で ``activate.ps1`` が呼ばれる。

.. code-block:: json

   {
     "python.pythonPath": ".venv\\Scripts\\python.exe"
   }


が、このままだとスクリプトの実行権限がないため、アクティベートできず困ってしまう。


.. literalinclude:: ./venv-activate-error.txt
   :language: text

2. activateするには
===================

アクティベートの過程では、 ``.venv/Scripts/Activate.ps1`` が呼ばれる。
しかし、初期状態ではps1スクリプトの実行ができなくなっており、アクティベートに失敗する。

真っ先に出てくるのは、ターミナル実行後に ``Set-ExecutionPolicy RemoteSigned -Scope Process`` で実行ポリシーを変更する方法。 [#]_ [#]_
ただし、これだと毎回ターミナルを起動するたびにコマンドを実行しないといけないため面倒。

3. 安全・楽にactivateするには
=============================

上記の手法を取らなくても、実際には対応が可能となっている。

これは、

* PowerShellの起動時には環境変数をちゃんとロードできる
* VSCodeではターミナル起動時に環境を設定できる [#]_
* PowerShellの実行ポリシーは、環境変数で切り替えることができる [#]_

という3点が成立するため、「settings.jsonに実行ポリシーに関する環境変数を設定する」ことで、容易に・他アプリへの影響を与えずに対応が可能となる。

.. code-block:: json

   {
     "terminal.integrated.env.windows": {
       "PSExecutionPolicyPreference": "RemoteSigned"
     }
   }

.. literalinclude:: ./venv-activate-valid.txt
   :language: text

.. [#] https://kb.upken.jp/UKowIVVgzmHkzszcugFEZrakoaxQrQ.html
.. [#] https://qiita.com/ryu22e/items/520b35db6a444d8289da
.. [#] http://serkanh.github.io/vscode,terminal,/2018/10/15/set-up-vscode-terminal-env-var.html
.. [#] https://tech.guitarrapc.com/entry/2016/06/04/035324
