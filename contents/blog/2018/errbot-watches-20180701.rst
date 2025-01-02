========================================
Errbotの動向追跡(2018/07/01版)
========================================

.. post:: 2018-07-01
   :category: Tech
   :tags: Python,Errbot,OSS,

定期的なアウトプットの訓練として、
ErrbotのGHプロジェクトの動向を雑にまとめてます。

先週できなかったので、2週分まとめて整理

Commits
=======

fix: Remove extra spaces in uptime output
-----------------------------------------

https://github.com/errbotio/errbot/commit/57422b89937da4d586f8fc03395b292dc09d3195

``uptime`` コマンドはlinuxのそれとだいたい同じで、「起動時からの経過時刻」を教えてくれるコマンドです。

``uptime`` コマンドの返信内容には、「経過時刻」「初回起動日時」「コマンド呼出時の引数」を返していたのですが、
このコミットで「コマンド呼出時の引数」がさくじょされました。

個人的な感覚では、``uptime`` コマンドに経過時刻以上の情報はあまり求めることもないし、
引数で挙動が代わるイメージもないため、妥当なコミットかなという印象です。

Issues
======

#1233 Undefined name 'all_plugin_paths' in backend_plugin_manager.py
--------------------------------------------------------------------

https://github.com/errbotio/errbot/issues/1233

``all_plugin_paths`` という変数がないため、flake8がNGになるというIssue。

原因は `その上部で定義されている変数がall_plugins_pathsであるため。 <https://github.com/errbotio/errbot/blob/57422b89937da4d586f8fc03395b292dc09d3195/errbot/backend_plugin_manager.py#L28>`_

なので、PR出して直しちゃうのが手っ取り早そう。

#1234 Make a new feature to do github mundane tasks on the slack channel.
-------------------------------------------------------------------------

https://github.com/errbotio/errbot/issues/1234

Google翻訳を駆使して読む限り、「GitHubのIssue追加とアサインをErrbotを仲介してSlackでできるようになりたい」ような。

多分、Botプラグイン作ったほうが早そう。というかありそう。

PRs
===

#1232 bootstrap.py: Create data/ dir at runtime if missing.
-----------------------------------------------------------

https://github.com/errbotio/errbot/pull/1232

「起動時に ``data`` フォルダがない場合には作成したい」というもの。
このPRはマージされずにクローズしています。

コメントによると、

::

  「ユーザーが間違っていたら、そこに勝手にフォルダを作るのではなく、おかしいと伝える」

という方向性のようです。
