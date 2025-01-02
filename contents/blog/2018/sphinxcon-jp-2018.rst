sphinx-revealjsを作ってSphinxCon JP 2018でトークした
====================================================

.. post:: 2018-12-10
   :category: Tech
   :tags: Python,Sphinx,Reveal.js,sphinx-revealjs,技術イベント,登壇,OSS,

少し時間が経過してしまったけれど、sphinx-revealjsを0.4.0へ更新したので、
ちゃんとブログとして書くことに。

SphinxCon JP 2018
-----------------

11月の終わりに `SphinxCon JP 2018 <http://sphinx-users.jp/event/20181128_sphinxconjp/index.html>`_ が開催され、
通常トーク枠として「素材の良さを活かしつつ、reSTをReveal.jsに変換してみる話」というタイトルで発表した。

https://attakei.gitlab.io/slides/talks/sphinxcon-jp-2018

10分枠だったのですが、話をまとめきれずに予定を少々オーバーしてしまった。ちょっと反省。

内容としては、 通常のHTMLビルドでの生成内容をベースに``sphinx-revealjs`` の中身を交えつつ、
「ここが嫌だからこうした」というものがメイン。
Revael.jsのくだりと準備不足が問題だろうれど、もう少しReveal.jsに寄せても良かったなとも思える反応だった。

.. textlint-disable

自分の発表も含めて ``docutils`` と向き合う系のトークがそこそこ多かった気がする。

.. textlint-enable

その他にも特定のライブラリに閉じたイベントのため、ハイコンテクスト気味な濃い目のトークが聞けて楽しい時間だった。

sphinx-revealjsもう少し深堀り
-----------------------------

Sphinxで次のことを実現することを目的とした拡張。

* なるべく「素のreST」をReveal.jsのプレゼンテーションに変換
* それぞれのプレゼンテーションで別々のRevealjsテーマにすることが可能
* この2点を備えることで、複数のプレゼンテーションを「Sphinxドキュメンテーション」として管理できるようにする

自分の中では、「Sphinx + Reveal.js」で代表的なものと思っているのは、
``sphinxjp.themes.revealjs`` で、ちょっとこれとの違いを簡単に整理する。
比較項目を見てもらえれば、「素のreST」を意識して作っているかが現れている。

後発なのと、特に露出の機会もそんなに多くないため、GitHub star数はこちらが圧倒的に少ない。

* プレゼンテーション生成

  * ``sphinxjp.themes.revealjs`` : ``html`` ビルド
  * ``sphinx-revealjs`` : ``revealjs`` ビルド(追加)

* Reveal.jsセクションの実現

  * ``sphinxjp.themes.revealjs`` : ディレクティブによる囲み
  * ``sphinx-revealjs`` : reSTのセクションノードをベースにする

* スピーカーノートの実現

  * ``sphinxjp.themes.revealjs`` : ディレクティブによる囲み
  * ``sphinx-revealjs`` : reSTのコメントをベースにする

.. textlint-disable

自分はメインPCがLinuxで、
「評価値の高いOffice系ソフトはない」
「大きな発表が少ないためHTMLスライドで十分やっていける」
みたいなことがあるため、
ある程度きちんとドッグフーディングしつつ、欲しい機能を追加しながらメンテしたいと思う。

.. textlint-enable
