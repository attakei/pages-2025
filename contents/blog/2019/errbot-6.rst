==========================
Errbot 6.0.0の更新内容整理
==========================

.. post:: 2019-04-28
   :category: Tech
   :tags: Python,Errbot,OSS,

Pythonのコードを書く時間を取れなくなっている間に、Errbotの6.0.0がリリースされました。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">Errbot 6 is out!<a href="https://t.co/HxlfXegZxK">https://t.co/HxlfXegZxK</a></p>&mdash; gbin (@gbin) <a href="https://twitter.com/gbin/status/1109642410638958593?ref_src=twsrc%5Etfw">2019年3月24日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

いろんな方面でのリハビリを兼ねて、1個前のバージョンである5.2.0との差分を追ってみようと思います。

前提
====

* Before: `5.2.0 <https://github.com/errbotio/errbot/releases/tag/5.2.0>`_
* After: `6.0.0 <https://github.com/errbotio/errbot/releases/tag/6.0.0>`_

Pythonのバージョン
==================

.. code-block:: diff

   $ diff errbot-5.2.0/setup.py errbot-6.0.0/setup.py
   24c24
   < PY35_OR_GREATER = py_version >= (3, 5)
   ---
   > PY37_OR_GREATER = py_version >= (3, 7)
   28,29c28,29
   < if py_version < (3, 4):
   <     raise RuntimeError('Errbot requires Python 3.4 or later')
   ---
   > if py_version < (3, 6):
   >     raise RuntimeError('Errbot requires Python 3.6 or later')
   49,51c46,47
   < if not PY35_OR_GREATER:
   <     deps += ['typing', ]  # backward compatibility for 3.3 and 3.4
   <
   ---
   > if not PY37_OR_GREATER:
   >     deps += ['dataclasses']  # backward compatibility for 3.3->3.6 for dataclasses

今回のバージョンから、Python 3.6以上が必須になりました。
また、Python 3.7を前提にしているからか、バックポート系の依存関係のカバーをするための変数が用意されています。

依存ライブラリ
==============

.. code-block:: diff

   $ diff errbot-5.2.0/setup.py errbot-6.0.0/setup.py
   35,36c35
   <         'bottle',
   <         'rocket-errbot',
   ---
   >         'flask',
   41,42c40
   <         'yapsy>=1.11',  # new contract for plugin instantiation
   <         'markdown',  # rendering stuff
   ---
   >         'markdown<3.0',  # rendering stuff, 3.0+ deprecates 'safe()'
   46d43
   <         'dnspython3',

全体的に大きな変更が入ってます。

* Webhookに使っていたWebアプリケーションのベースが、BottleからFlaskへ変更
* Pluginの管理を行うPluginManagerが、yapsyの依存を脱却

コアの挙動に影響しそうなのがこのあたりの変更かなと思います。
時間を取れればこの辺をどうして変えたかを考えてみたいですね。

差分の概要を眺める
==================

``diff -r errbot-5.2.0 errbot-6.0.0`` を実行すると、目につくのはこれらがほとんど。

* f-string採用、loggerへのログ渡し方などの文字列表現の整理
* 現状のコーディング規約への統一（関数定義時の仮引数まわり）
* Logger作成時の名前指定が、文字列固定から ``__name__`` へ

ぼーっと眺めて回る感じだと、目立った変更っぽいのがこのあたりです。

* ``errbot/bootstrap.py``
* ``errbot/core_plugins/webserver.py``
* ``errbot/plugin_manager.py``
* ``errbot/repo_manager.py``

目につく変更ピックアップ
========================

errbot/bootstrap.py
-------------------

``setup_bot`` において、プラグインマネージャーの作成順が変わりました。
さらに、try〜exceptの範囲が広がり、Backendプラグイン起動後からセットアップ完了までのExceptionをすべて拾うようにました。

全体的に、起動の過程が安定して完了するように処理され、処理失敗時にはきちんと失敗するようにされているように見えます。

errbot/core_plugins/webserver.py
--------------------------------

``Bottle + Rocket`` が ``Flask`` へ変更されたことに合わせてか、 ``activate`` 内での処理が若干変わりました。

* Before: WebserverはRocketのインスタンスを管理するだけで、Rocket起動時に内部でスレッドを管理
* After: Webserverプラグインがスレッドを管理して、スレッド内でFlaskサーバーを起動

実態としてはErrbotを使う側で特に意識すべき点はおそらくほぼなく、
逆にコア周りを取り扱う人はもしかしたらFlaskプラグインを突っ込めて良いのではないかな？と思いました。

errbot/plugin_manager.py
------------------------

プラグイン管理がYaspyベースでなくなり、大きく改変されてます。
（あくまで内部的な実装の変更であり、実際のチャット側からは、変わらず `!repos install` でインストールができます）

Webserverの変更と違い、「Yapsyベース」→「自前」という変更のため、一度余裕を見つけて、もう少し深堀りしてみようと思います。

また、パッケージインストール時において、Dockerを考慮するようになりました。

errbot/repo_manager.py
----------------------

``check_dependenceis()`` 関数が、 ``plugin_manager.py`` から引っ越してきました。
プラグイン管理の仕様変更で、依存パッケージの考え方がリポジトリ管理に重点を置くことになった？とかでしょうか。

変更の影響は？
==============

最古の自作プラグインである、 ``jp-weather`` が何事もなくインストールできて、なおかつ普通に動きます。

結構コアな部分に変更がかかっても、インターフェースレベルでの変更なしに動くのは、
テストケースの存在が正しく機能していると考えられるため、ここは見習いたいなと感じました。

まとめ
======

普段使う分には大きな変化はそこまで無いものの、「古いコードの適切な廃棄」「外部依存を減らす」が進行していっています。

アルファバージョンの時期がかなり長かったのですが、ゆっくりと更新されていくでしょう。
