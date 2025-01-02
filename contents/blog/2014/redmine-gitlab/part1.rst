====================================
Redmine + gitlab 連携で躓いた(その1)
====================================

.. post:: 2014-10-20
   :category: Tech
   :tags: nginx,Ruby,Redmine,GitLab,

ちょっと、ALMiniumによるredmine+gitではなく、redmineプロジェクトに同期しないリポジトリも置きたくなった。

そこで一旦ALMiniumから離れて、Redmine, GitLab, Jenkinsなどをnginxをフロントにして個別インストールすることに。

で、こんな感じ盛大に躓いて半日以上潰したのでメモっとく

redmine, gitlabのインストール
=============================

単純にインストールしてアクセス確認するまでは、ほとんど躓かなかった。

nginxをフロントに据える
=======================

最初に少々躓いたところ。

Redmineのインストール先を、わりと一般的な **/var/lib/redmine** ではなくしたのが過ち。

やりたかったこと
----------------

* redmineユーザを作成して、/home/redmine/redmine にcloneして動かす
* UnicornでRedmineを動かし、nginx向けにはポートリッスンではなくsokectを使う

起きたこと
----------

nginxが403しか返さない。error.logには ``Permission denied`` と出るが、socketのパーミッションだと思い込んで、
777にしたものの変化なし。

原因
----

/home/redmine 自体にnginxユーザがアクセスできてない...
nginx,redmineを同じgroupにしたうえで、/home/redmineをgroupも実行可にしてどうにか通った... [#]_

.. code:: bash

   # groupadd service
   # usermod -G service,nginx nginx
   # usermod -G service,redmine redmine
   # chmod 775 /home/redmine

redmine + gitlab のユーザ認証を連携させようとしたが...
======================================================

gitlabを入れても認証がバラけるのは面倒だったので、ユーザ管理は基本redmineに任せる。

* どちらも、unicornで動かして、nginxがproxy_passでアクセス
* /redmine, /gitlabという形式でサブディレクトリ構成にする
* redmineに redmine-oath-provider をインストールして認証元へ
* gitlabに omniauth-redmine をインストールして認証先をredmineへ
* 下がnginxのconfの一部(必要そうなところ)

.. code::

   server {
       server_name myserver;

       location ~ /redmine {
           access_log /var/log/nginx/redmine_access.log;
           proxy_pass http://redmine;
       }

       location ~ /gitlab {
           access_log /var/log/nginx/gitlab_access.log;
           proxy_pass http://gitlab;
       }

   }

この設定で、gitlabのredmine認証ページ(/gitlab/users/auth/redmine)へ進もうとしても、Not Foundとしか出ず。
gitlab側のログ類をチェックしても、ログレベルを下げても何も出てこない。

しばらく他のログを見回してみると、Not Foundのログがredmine側に出ているのに気づいたのが一旦諦めて日付が変わった後。

gitlab側のURLなのに **/redmine** が含まれているので、redmine側で処理されてしまったらしい。

**^** を追加することでどうにか解消できた。

.. code::

   server {
       server_name myserver;

       location ~ ^/redmine {
           access_log /var/log/nginx/redmine_access.log;
           proxy_pass http://redmine;
       }

       location ~ ^/gitlab {
           access_log /var/log/nginx/gitlab_access.log;
           proxy_pass http://gitlab;
       }

   }


これでOauth認証のフローは進むようになったのだが、別のトラブルが発生。
直した分は別記事にまとめる途中。

.. [#] gitlabのインストールをトライした時にも同じ目にあったはずなのに…
