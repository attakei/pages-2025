==========================
PyCon JP 2019 の参加側感想
==========================

.. post:: 2019-09-19
   :category: Tech
   :tags: 技術イベント,Python,PyCon JP,
   :redirect: blog/2019/pyconjp-2019/attendee

PyCon JPに参加したので、一般参加枠視点での感想です。

ちなみにですが、例年にも増して、午前中のセッションを聞きに行く余裕はありませんでした

Day 1 トーク感想
================

Yet Another Isolation - Debian Packageと紐づく環境分離
------------------------------------------------------

* https://www.youtube.com/watch?v=e9MKpn8bqx4
* https://speakerdeck.com/puhitaku/yet-another-isolation-debian-packagetoniu-dukuhuan-jing-fen-li
* https://github.com/groove-x/gxenv

GROOVE Xの方による、Debian環境下におけるPyhonパッケージに関する話。

* OSのパッケージリポジトリで管理されているものと、自分がほしいものにギャップ
* 単純な仮想環境(venv)では、環境が散らばる

といった点を解決するために、pyenvやPipenvなどを使わずに、あえてgxenvとうライブラリを自作した模様。

.. textlint-disable

「環境が持つ問題点を整理」→「一般的な解放の特性を調べて、フィットするかを精査」という流れを経て、
「存在しないのであれば、作るしかないよね」みたいな発想は、大切だなとは感じました。

.. textlint-enable

Python ウェブアプリケーションのためのプロファイラの実装
-------------------------------------------------------

* https://www.youtube.com/watch?v=ojnVMGon5d4
* https://speakerdeck.com/ymyzk/implementation-of-a-profiler-for-python-web-applications
* https://github.com/ymyzk/wsgi_lineprof

個人プロジェクトである ``wsgi_lineprof`` をもとにしたプロファイラー開発の話。

WSGIミドルウェアという実装をとってることで、WSGI全般に組み込めるのは非常に良さそう。
こういった話を聞くと、いかに「ミドルウェアを挟めるか」「プラガブルか」に気をつけて実装することの意味を感じられる話でした。

それにしても、パフォーマンスを求められてくると、やっぱりCPython自体やCythonあたりを見ないとだめかなとはなりますね。

ListはIteratorですか？
----------------------

* https://www.youtube.com/watch?v=Ig6X6VH15RY
* https://docs.google.com/presentation/d/1mXOBuUIG_jlyKwxO792Nk6WQphyts2uuerPkDarwGFg/edit?usp=sharing

「Iteratorの人」によるイテレーターの話。自己紹介より前にタイトルの主題を回収するという、他とはちょっと違う感じのスタイル。

内容としては、上記をメインに据えた上での、Typing周りの話など。
型ヒントって、かなり細かくインターフェースレベルで分割してあるんですね。

個人的にはこういったPythonの内部挙動寄りの話を聞くのが結構好きで、
Pythonコードの振る舞いについての意識を強める機会をくれるので、大変助かります。

mypyそろそろ使おうかな...

Day 2 トーク感想
=================

婚活・恋活領域におけるPythonを使ったマッチング最適化
----------------------------------------------------

* https://www.slideshare.net/TakashiMorioka/python-172910459

Dine社の人による。Dineの中身のマッチング実装に関する話。意向によりYouTube配信は無しで。

完全異業界なので、業界感ある表現があってなかなか楽しかったです。安定結婚問題とか。

システム面では、ちょこちょこ出てくる「GAEの見えない天井」がなかなか難儀そう。
発表を見る限り、Dataflowはかなり強力そうに見えるけれど、文法がちょっと自分にはなじまないかも？

入門 自作検索エンジン
---------------------

* https://www.youtube.com/watch?v=5EEH8MHfAyA
* https://speakerdeck.com/ryook/the-first-step-self-made-full-text-search

全文検索の概要とその作成事例。

エンジニアが全文検索エンジンを習作するのにちょうどよいエッセンスかなという印象。
丁寧にステップを踏んでくれているっぽい。

「AND or ORの全文検索とイメージとの乖離」みたいなものも感じられて、なかなか意義深かったです。

新米Pythonistaが贈るAirflow入門 & 活用事例紹介
----------------------------------------------

* https://www.youtube.com/watch?v=T0JVQWfnRAo
* https://speakerdeck.com/matsudan/pyconjp-2019-xin-mi-pythonistagazeng-ruairflowru-men-and-huo-yong-shi-li-shao-jie

文字通りAirflowの入門発表。

LT/クロージング系トーク 感想を雑多に
====================================

* 特にLTが全体的に表示サイズがアンマッチだったような。飛び込みLTがあるなら、表示レギュレーションは全公開で良かったかもしれない [#]_
* 結局パッケージの話があるじゃないか。1分半しか使ってないw
* オレオレブラウザという発想がすごい。
* Xonshちょっと離れてたけど、Windowsで普通に使える匂いに気づいた。
* 例年ネットワークチームには感謝してるけど、今回もヒートマップが時間帯を示してて面白かったです。
* Twitterでもポストしたけど、リジェクトコンは可能な限り参加したいです。
* 商標周りに関する件があったが、PSFが表明をしてくれるっぽい。
* 来年のは8月末の金土。アニサマと被らないかがちょっと心配。

その他
======

* ドリンク・ランチ・おやつ・パーティーと飲食系は今年も充実。
* D会議室のセッションの人気度が、多分スタッフも想定外のレベルで高かったっぽいですね。調整難しそう。
* 別会場でライブストリーミングの配信など、丁寧に対応してくれたとは思います。

.. [#] 発表者側にはPapercall経由で通達されました
