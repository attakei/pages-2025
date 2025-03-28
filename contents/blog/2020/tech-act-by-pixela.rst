==========================================
雑多な技術系アクティビティをPixelaに溜める
==========================================

.. post:: 2020-10-04
   :category: Tech
   :tags: Nim,Pixela,teratail,

アクティビティをひとまとめにした草が欲しくなりました

技術アクティビティ
==================

技術系の情報発信・コミュニケーションにはいくつかの手段があります。

普段自分がなにかやってるときだと、

* GitHub: OSS関連
* GitLab: その他個人ソース関連
* teratail: 回答
* Qiita/zenn/devto: 記事書くとか

あたりがあります。

GitHub(GitLab)にはこのあたりのアクティビティを視覚的に俯瞰出来る通称「草」という便利な仕様があります。
が、他のサイトでは無かったり、そもそも複数をまたいでいると分かりづらかったりします。

今回は自分用に、書くアクティビティを集計してスコア付した値を視覚化してみることしました。

push/pullツール"tact"
=====================

この記事時点で、やってること

* ``pull`` コマンドで、各アクティビティを集計
* ``push`` コマンドで、この結果をPixelaにポスト

今は、集計元がteratailだけなのと、単純な回答回数のみをスコアとしていますが、
ちょこちょこ機能を足して「アクティビティスコア」を表現出来るようにするのをゴールとする予定です。

ゴールは↑で上げたサイトの集計とスコア化して、定期実行でポストする状態です。

ソース
------

https://github.com/attakei/tact

コードについては、Nimで書きました。

なんでNim?
==========

ざっくり書くとこんな理由です。

* バイナリコンパイルをする言語の選択肢を持ってみたかった
* オフサイドルールな言語としてNimが目についた
* Golangも考えたけど、あえて戦略とか度外したくなった結果除外

感想は？
--------

「PythonのふりをしきれないC」というのが感想です。

バイナリ実行であるがゆえに、実行速度はやっぱり速いですね。
書き味の部分がPythonっぽさでラップされているので、速度を求められる時の選択肢としてはありかなと思いました。

※今回のに適しているかは疑問

Nimbleを経由したサードパーティ製ライブラリもあるので、
低レイヤーな箇所はそこまで自分で実装しなくて済むのは良いですね。
ただ、ユーザー人口かそんなに多くない印象。

JSトラスパイルもあるので、今度試してみたいです。
