ALMiniumのインストールで気をつけたことetc
===========================================

.. post:: 2014-05-15
   :category: Tech
   :tags: ALMinium,

ちょっと大して重要ではない細々とした理由で、今とは別の環境でALMiniumをインストールしてしてみた。
で、実際に作業した際になんとなく引っかかったりしたことをメモっていく。

前提
----

* インストールは2014/05/13に実施
* httpsを有効化
* Jenkinsを同時にインストール
* 個人的な嗜好により、reStructuredText formatterを追加でインストール


インストールするまで
--------------------

前回インストールしてみた時と変わらずに簡単にできる印象。


httpsを有効化してみたら……
-------------------------

redmine側は特に問題らしい問題が無かったのだけれど、そのままjenkinsへ移動すると、毎回リンクでの遷移が引っかかる。

今回も前回同様にサーバ自体はhttpsのみを受け付けるようにしたため、jenkinsのデフォルトでhttpへ遷移しようとしていた模様。
設定を切り替えていってどうにかできた。

reStructuredText formatter
--------------------------

RbST/docutils versionに基いてインストールし用とした際に躓いた点と対応をメモ

* "script/plugin install"に失敗。script/pluginが見つからない
    * A:いつからなのかはわからないけど、"script/rails plugin"に変わったっぽい？
* 上に気づいても、何故かcloneに失敗？

で結局、次の手順でインストール

.. code-block:: bash

   # cd /path/to/redmine
   # cd ./plugins
   # hg clone https://bitbucket.org/ebrahim/redmine_restructuredtext_formatter
   # chown -R apache:apache redmine_restructuredtext_formatter
   # cd ..
   # bundle install
   # service httpd restart

動いているのでOKとしておく。

あとは、WindowsAzure上に置いているので、これがMSDNでもらえているクレジットを越えないことを祈るのみ。
