==============================
Sphinx+翻訳 Hack-a-thon 2025.1
==============================

.. post:: 2025-01-15
   :category: Tech
   :tags: Python,Sphinx,sphinxjp,Zenn,

年始も元気にSphinx関連作業を進める時間を確保しています。

https://sphinxjp.connpass.com/event/341157/

atsphinx-goto-top
=================

SphinxのHTMLビルドに対して、画面下に「トップに戻る」ボタンを付与する拡張を作ってました。 [#]_
`The PyData Sphinx Theme <https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html>`_
のようにテーマに組み込まれているケースもあるのに対して、今回作ったのは「どのテーマでも使える」ことを意識したものです。

.. [#] 実際に作ってたのは少し前で、実際に当日はドキュメント作成とリリースが中心でした。

薄く実装したので、ドキュメントにあるものと違って、このサイト上で表示されるようなカスタマイズも容易だったりします。 [#]_

.. [#] もちろん、簡単なHTML,JS,CSSの知識は必要ですが。

i18n対応したら需要がありそうなので、もう少し開発をしてみる予定です。

リンク
------

* `PyPIプロジェクト <https://pypi.org/project/atsphinx-goto-top>`_
* `GitHubリポジトリ <https://github.com/atsphinx/goto-top>`_
* `ドキュメント <https://atsphinx.github.io/goto-top/>`_
* `Zenn記事 <https://zenn.dev/attakei/articles/reelase-atsphinx-goto-top>`_

atsphinx-toybox.pyproject
=========================

前日にふと思いついて作ってみた、
「 ``pyproject.toml`` に記述した項目を ``sphinx-build`` 時の設定にする」という変わり種です。 [#]_
実用性はともかくとして、 Pythonプロジェクトのメタデータを ``setup.py`` ではなく
``setup.cfg`` に書くという変遷を眺めていた身としては、懐かしいスタイルが出来上がりました。

.. [#] Zenn記事の冒頭にも書いたのですが、完全に遊び半分で作ってます。

.. ogp-image:: https://zenn.dev/attakei/articles/sphinx-configuration-on-pyproject
   :align: center
   :width: 50%

リンク
------

* `ドキュメント <https://atsphinx.github.io/toybox/en/utils/pyproject/>`_
* `Zenn記事 <https://zenn.dev/attakei/articles/sphinx-configuration-on-pyproject>`_
