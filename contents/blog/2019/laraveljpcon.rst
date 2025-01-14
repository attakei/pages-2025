===================================================
Laravel JP Conferenceに参加して、LT枠で喋ってました
===================================================

.. post:: 2019-02-21
   :category: Tech
   :tags: PHP,Laravel,LT,技術イベント,登壇,

「小ネタ喋って懇親会」メソッドを実践してみようと思い、
LTのCfPを出したら採択されたので、
勢いで参加しました。

https://conference2019.laravel.jp/

喋ったこと
==========

`こちらのHTMLスライドです <https://attakei.gitlab.io/slides/talks/laraveljpcon-2019.html>`_

Perl-CGIから続いている「アクセスカウンター」をLaravelの仕組みで作る、
という自分の中でも発展性の薄いテーマで参加しました。
よりによってトップバッターだったのですが、狙いにいったタイミングで会場が湧いたので、成功かな？と思います。

* 5分たったらドラが鳴ります
* ドラが鳴ったら、巻いてください

という温情のおかげで、ロスタイムを数秒消費して無事にスライドは出し切れました。
前日中途半端な状態で素振りに付き合ってくれた社内の人には感謝。

聞いてたトークの感想等
======================

Laravelでパッケージ開発
-----------------------

* https://fortee.jp/laravel-jp-conference-2019/proposal/bdd3c73b-9e25-4c09-9379-9771b4605092
* https://speakerdeck.com/mikakane/laravel-package-development

Laravelにおけるパッケージ機能を用いた機能分離の話。
自分の主眼としては、パッケージ機能の存在を知られたことが一番大きく、
のちほどアクセスカウンターをきれいにライブラリにするための知見が得られてよかった。

機能分離については、、、社内でそんなシーンができそうなら紹介してみようかと。

Webアプリケーションが今こそ知るべき、RDBMSのパフォーマンスチューニングの勘所 ～未踏の速度を目指して～
-----------------------------------------------------------------------------------------------------

* https://fortee.jp/laravel-jp-conference-2019/proposal/e095a99c-dddd-4862-952e-fe83046fed38
* https://speakerdeck.com/soudai/basic-of-rdb

開始宣言の通り、ほぼほぼデータベースの話をしなかったセッション。

それでも、初診に帰ってデータベースの使い方を見定めるのにはいい時間だったと思う。

抽象化って何？
--------------

* https://fortee.jp/laravel-jp-conference-2019/proposal/636c1bdb-ea9e-4b53-af9e-ac3839d4596c
* https://speakerdeck.com/hidenorigoto/chou-xiang-hua-tutehe-what-is-abstraction

「抽象化」の考え方と、その考え方をプログラミングに落とし込むときの指針などについて。

『抽象のはしご』に基づく抽象化と具体化の行き来は効きながら考えるとしっくりくるのと、
そこから進んだプログラムにおける抽象化は納得感がかなりあった。
その分、直近で書いたコードが正しく抽象化できたのかが不安になる。

まとめ的なの
============

Laravel TrackではLaravelの深めの話を聞けて、PHP Trackではそれこそ言語を問わない強い話を聞けてと、充実した一日でした。
普段PHPをほぼ書かない系の人でも暖かくLTLTさせてくれたのには、本当に感謝しかありません。

一応来年は予定されていないのですが、誰かが来年の企画をした際には、ぜひ盛り上げたいと思います。
