atsphinx-mini18n v0.4.1
=======================

.. post:: 2025-05-20
   :category: Tech
   :tags: Python,Sphinx

https://pypi.org/project/atsphinx-mini18n/0.4.1/

ちょっとIssueをもらったのですが、最終的にBug扱いで良さそうだったので修正リリースまで出してました。

..
   TODO: Use ogp-image

.. figure:: https://opengraph.githubassets.com/897b7c058fe3f489f1bba4be28e902ccfc6b421e1293cd11918f0e05a97d5e3f/atsphinx/mini18n/issues/6
   :target: https://github.com/atsphinx/mini18n/issues/6
   :width: 50%

何を直したのか？
----------------

Sphinxのテンプレート内で、ドキュメント名（ ``pagename`` ）からURLを組み立てる方法が ``pathto`` しか思いつかなかったのですが、
その関係で ``pathto(pagename, 0, '.')`` と呼び出して「自分自身から見た自分のパス」を作ってました。

ところが、 :pypi:`sphinx-notfound-page` と組み合わさると「上書きされた ``pathto`` が第3引数に相対パスを受け付けない」挙動になり、
ビルドに失敗していたようです。

基本的に、外的要因はBugとするべきかが難しいのですが、見返す過程で程よい実装案を思いついたので、
そのままBug扱いして実装+リリースまでしています。

ちなみに、実装的には「専用のAlt ``pathto`` を実装しておく」というもの。
``atsphinx-mini18n`` は構造的にFQDN以下の絶対パスを組み立てるの必要な情報を全て揃えていたので、
最初から独自で組み立てるほうが楽という判断になりました。

ついでに
--------

* せっかくなので、AlphaステージからBetaステージへ。
  これは、自分以外のユースケースが登場したことによるものです。
* だいぶ期間があってたからかPython 3.13のサポートが明記されていなかったので記載。
  Python 3.8がまだ有効だったのですが、別の実装とセットで消してしまおうかなと。
* プロジェクトワークスペースの管理方法を現行に寄せてみました。
* 試しに別ブランチで :pypi:`ty` を組み込み中。
  速度がかなり出るので、常時使っていてもストレスにはならなそうです。
