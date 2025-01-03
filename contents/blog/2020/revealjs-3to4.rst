=========================================================
Reveal.jsプレゼンテーションのバージョン切り替えメモ(3->4)
=========================================================

.. post:: 2020-11-17
   :category: Tech
   :tags: Python,Reveal.js,sphinx-revealjs,

``sphinx-revealjs`` のバージョン更新のために、
Reveal.jsのメジャーバージョンの差異を、中間開発者視点で再整理してみました。

前提環境
========

* ``sphinx-revealjs`` のデモプレゼンテーションをいじる
* 3.x系は3.9.2
* 4.x系は4.1.0

前提として
==========

Reveal.jsのドキュメントには、アップグレードガイドが載っています。
ので、基本的にはそれを読みつつ、文字に落とし込み直す形となります。

https://revealjs.com/upgrading/

コンバート勘所
==============

基本的なファイル指定
--------------------

プロジェクト管理の構造が整理されて、コアファイル系の配置が変わってます。

以前は、 ``css`` , ``js`` が別フォルダになっていたものが、
通常利用のためのファイルが ``dist`` に出力されるようになりました。

.. code-block:: diff

    -<link rel="stylesheet" href="_static/reveal.js-3.9.2/css/reveal.css" type="text/css" />
    -<link rel="stylesheet" href="_static/reveal.js-3.9.2/css/theme/black.css" type="text/css" />
    +<link rel="stylesheet" href="_static/reveal.js-4.1.0/dist/reveal.css" type="text/css" />
    +<link rel="stylesheet" href="_static/reveal.js-4.1.0/dist/theme/black.css" type="text/css" />

    -<script src="_static/reveal.js-3.9.2/js/reveal.js"></script>
    +<script src="_static/reveal.js-4.1.0/dist/reveal.js"></script>

印刷用CSSの指定が不要に
-----------------------

``dist/reveal.css`` に印刷用CSSである ``css/print.pdf.css`` などがバンドルされるようになったようです。
そのため、 ``css`` フォルダを完全に無視できるだけでなく、
印刷系設定のためにJavaScriptを記述子なくてよくなりました。

.. code-block:: diff

    -<!-- Printing and PDF exports -->
    -<script>
    -┆ ┆ var link = document.createElement( "link" );
    -┆ ┆ link.rel = "stylesheet";
    -┆ ┆ link.type = "text/css";
    -┆ ┆ if (window.location.search.match( /print-pdf/gi )) {
    -┆ ┆ ┆ ┆ link.href = "_static/revealjs/css/print/pdf.css";
    -┆ ┆ } else {
    -┆ ┆ ┆ ┆ link.href = "_static/revealjs/css/print/paper.css";
    -┆ ┆ }
    -┆ ┆ document.getElementsByTagName( "head" )[0].appendChild( link );
    -</script>

プラグインの利用方法の変化
--------------------------

プラグイン自体が ``plugin`` フォルダにある事自体は変わってません。
ただし、Reveal.jsコア側での基本的なプラグイン利用方法が大きく変わっています。

以前は、 ``Reveal.initialize()`` のオプションとして、依存ファイルを直接指定する仕様でした。
今回からは、ソースの読み取りと初期化のプロセスが別になりました。

.. code-block:: diff

    +<script src="_static/reveal.js-4.1.0/plugin/notes/notes.js"></script>
    <script>
        var revealjsConfig = {
    -        dependencies: []
    +        plugins: []
        };

    -    revealjsConfig.dependencies.push({
    -        src: "_static/reveal.js-3.9.2/plugin/notes/notes.js",
    -        async: true,
    -    });
    +    revealjsConfig.plugins.push(RevealNotes);

        Reveal.initialize(revealjsConfig);
    </script>

余談
^^^^

* しれっとHighlightモジュール用のCSSがプラグイン側に引っ越してます


sphinx-revealjs視点での感覚
===========================

コアファイルに関しては、単純に場所が変わっただけなのでさほど気になりません。
印刷用CSSに関しても不要になっただけなので考慮負荷は大して無さそうです。

問題はプラグイン。

パスのみを考慮すればよかった実装から、クラス名を確保しないといけなくなったため、
conf側で用意しないといけない情報が増えてしまいそうです。

既存の方式か、ESモジュール形式か
--------------------------------

Sphinxの視点からだと、各々このような違いがあります。

- 既存の方式

  - ``<script>`` にファイル指定が出来るので、他のjsと読み込み周りの挙動に差が発生しない
  - クラス名がグローバルで固定のため、ユーザー設定側で正しいものを指定しないといけない

- ESモジュール形式

  - クラス名を勝手に決められる可能性がある（ ``import`` 構文で好きに決めて良いかもしれない）
  - ``.esm.js`` は完全に別指定しないといけない

振る舞いに差がなく、そもそもプラグインの設定変更などが出来なさそうなことを考えると、
当面の間は無理にESモジュール形式で出力必要もなさそうです。

あとがき
========

見た目の破壊的変更はそこそこの量がありはするのですが、
細かく分解していくと割合と一個単位ではシンプルな対応ができそうです。

後は、v3とv4を同梱させるか、それとも次の時点でv3を切り捨てるか...
