===========
ABlog試し中
===========

.. post:: 2019-11-28
   :category: Tech
   :tags: Python,Sphinx,ABlog,

Static Contents Generatingな部分の基盤を ``Sphinx`` に集約しようかなと思い立って、
ABlogを試している。
ダメでも「ダメだった」共有のつもりで、序盤から試行錯誤などをブログ記事としてまとめてみる。

サイトの構造
============

* ``Sphinx`` 上に、「ブログ」「スライド」「それ以外のページ」が一通り載ってる
* ビルド自体は、 ``conf.py`` でやりくりして「スライド」「それ以外」で分ける
* これを、過去資産を引き継ぎつつ、Sphinxプロジェクトとしてまっさらな状態からスタート

経過ログ
========

* 11/28 トライアル開始。

トピック
========

素のsphinx-quickstartからABlogを始めたときに最低限必要な設定
------------------------------------------------------------

* https://ablog.readthedocs.io/index.html
* https://ablog.readthedocs.io/manual/ablog-configuration-options.html

素の状態から `ablog` を有効にするまでは問題ないけれど、
``make html`` が失敗してしまう。

.. code-block:: pytb

    Exception occurred:
      File ".venv\lib\site-packages\sphinx\builders\html.py", line 656, in gen_pages_from_extensions
        for pagename, context, template in pagelist:
    RuntimeError: generator raised StopIteration

どうも、「フィードを作るなら必須」と書いてある ``blog_baseurl`` が最低限文字列が何かないとダメだった模様。
原因は一旦放置。

.. code-block:: python

    # Options of ablog
    blog_path = 'blog'
    blog_baseurl = '/'

積極的にABlogのテンプレートを利用する
-------------------------------------

ABlogにはデフォルトではテーマを持っておらず、Alabaster+ABlog向けのパーツが基本となっている。

それに対して、Pelican用にテーマを作ってたので、単純にテーマとして移植しょうと思ったのが失敗だった。

現在は、シンプルに ``_templates`` フォルダにレイアウト用のテンプレートを置いてる。積極的にパーツを使ったほうが良い。
