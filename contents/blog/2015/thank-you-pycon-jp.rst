==================
Thank you PyCon JP
==================

.. post:: 2015-10-12
   :category: Tech
   :tags: 技術イベント,Python,PyCon JP,

ブログとかに感想エントリーとかを書くまでがカンファレンスって誰かが言ってた。

10/10,11に PyCon JP 2015 へ行ってきました。去年はランティス祭りと完全に被ってたので、日程が発表と同時に不参加だったので、今年が初参加。

セッションもろもろ
==================

1日目
-----

* Python と型ヒント (Type Hints)

  * 型ヒント自体はなかなかに興味深い。IDEがうまく使ってくれるだけでも、間違いなく有用であるとは思う。
  * 中途半端に実装系に使われてしまって、CPythonとPyPyで挙動がガラッと変わるとかがなければいいかな。

* なぜWeb画面自動テストはうまく行かないのか

  * Seleniumがコストを伴うのは仕方がないとしても、品質を担保するためにはある程度許容はすべきかと。
  * この辺は企業でのバランス感に依存したりするかな。

* Tornado/ElasticSearchで実現する大量ツイートのリアルタイム関連文書判定

  * ElasticSearchの話題がほとんどで、Tornadoの話が殆ど出てなかったような

* Sphinxで作る貢献しやすいドキュメント翻訳の仕組み

  * i18nって普段使わないので、使い方とか知るいい機会になった。
  * 日本語のドキュメントがあると敷居が下がるのは理解できる。なるべく自分は英語ドキュメントを積極的に読もうするのは、別の話になるだろうし。
  * 普段使っているパッケージのドキュメントがほとんど英語しかないので、機会があったら翻訳してみるのも悪くないかも。と思える、いいセッションでした。

2日目
-----

* Keynote

  * 組織論など。OSSコミュニティ的な組織は確かにうまく回せれば気持ちいので、組織内の人対人は役割ベースで動けるほうがいいとは思う。
  * 企業しての案件進行などを考えていくと難しい面もあると思うので、この辺は上の層が考えればいいのか？というかその方が楽（多分ダメだと思うけども）
  * ビープラウドの名刺面白いなぁ（役職欄がほぼ自由でウォーロックなんてのもあるとかw）

* uWSGI/Dockerを利用したWebサービス運用事例

  * gunicorn以外のWSGIとしてuWSGIの性能指標とノンストップサービスのためのサービスコントロールについて。
  * (自分はPyramidを普段使いしている&大規模ではない、のでもっぱらwaitressを使ってます)

* 野球Hack!~Pythonを用いたデータ分析と可視化

  * 去年のタイムラインを眺めてた際に、個人的に異彩を放っていたもの。事前判定でのメインセッション。
  * そして「趣味」+「エンジニアリング」の究極系の片鱗をみた気がする。
  * アダム・ダン率計算に続き、ジョーイ・ボットの散歩回数まで出てくる。
  * (ちょっと、これをきっかけにクイズHackとかやってみたくなるじゃないか)
  * スライドを振り返ると、Pythonパッケージでできる属性は結構多い…

  * PyPIデビュー 2015

  * 当日プログラムを見た時から真っ先に行くことが確定していたやつ。
  * 自分用に作ってたTinkerer用Twitterまとめエントリー作成用パッケージをPyPIには登録してみていたものの、きちんとした流れを追いたくて出席
  * スライドを教えてもらった瞬間で期待値を遥かに上回る収穫が

ランチやらパーティーやら
========================

普段懇親会やパーティーの類はほとんど出なかったのだけど、チケット代に入ってたりもしているのもあり参加してみることにした。

自分を含めて自称コミュ障が多い。が、そんなもんだとは思う。（パーティー時に会話したメンツの中では多分自分が一番コミュ障）

Pythonを主力にしている企業の人だけでなく、Pythonを仕事外で使っている人もいていろいろと楽しい会話ができたかなと。

まとめ
======

**Thank you PyCon JP!!**

また来年も行きたいし、セッション・LTあたりが出来るようになっていたいな、と思える2日でした。
