2025/04/14-の週を少し振り返ってみる
===================================

.. post:: 2025-04-22
   :category: Tech
   :tags: Pipedream,Prefect,1Password,Python,Sphinx,sphnix-revealjs

なんか先週に小トピック的なことをいくつかやってたので、整理がてら振り返ってみています。

sphinx-revealjs v3.2.0
----------------------

こんな記事を書いていました。

.. ogp-image:: https://zenn.dev/attakei/articles/compile-sphinx-revealjs-theme-3-2
   :width: 50%
   :align: center

最近ではsphinx-revealjsのIssue整理にマイルストーン機能を活用しだしていて、v3.2にあれこれ並んでいました。
ところが、予定外の事態に遭遇した関係で、別方面の機能を中心に追加したものとしてv3.2.0としています。

Zennに書いた今回の記事は、エッジケースにおいての事前対処方法を書いていたのですが、
他に引っかかる人が出る前に気づけてもらえればいいかなと。
もちろん、CHANGELOGSあたりには書いたつもりですが。

.. container:: is-justify-content-center is-flex

   .. oembed:: https://x.com/attakei/status/1912524830756544757

ZennにPipedream関連の記事を書いてた
-----------------------------------

Xへの投稿に困っていたので、他記事を参考にしつつカスタムアクションにしたやつ。

.. ogp-image:: https://zenn.dev/attakei/articles/pipedream-actions-x-tweet
   :width: 50%
   :align: center

同じようなことをBluesky向けに実現したやつ。 [#]_

.. ogp-image:: https://zenn.dev/attakei/articles/pipedream-actions-bluesky-linkcard
   :width: 50%
   :align: center

.. [#] Blueskyの場合は、「リンクカード」という構造にするためにはポストと独立したEmbedを登録する必要があるため、そのあたりに手間が必要だった。

……ちなみに、この時点でPipedreamのFree枠を使い潰しそうだったので、慌ててPrefectの再構築を試しているのが週末から今日の状況だったりします。

Prefect再入門
-------------

Prefect Cloudの無料環境をサーバー部分として利用しつつ、定期処理のワークフローを ``prefect serve`` の形式でモニタリングさせています。
ちなみにこちらのほうがジョブの登録可能数が多いのと、ジョブの融通が効きやすいというあたりがPipedreamとの雑比較です。 [#]_

常時稼働しているマシンでプロセスを動かしているので、最終的にはCloud部分を自分でサーバー稼働させる想定です。

.. [#] 根本的な用途が違うと言われれば、まぁそうとしか。

1Password for Open Source
-------------------------

sphinx-revealjs名義で申請して、無事に受理されました。
使用感などは :doc:`/notes/compute/service-with-for-oss-plan/1password` あたりにまとめていく予定です。

ほぼ同時進行でBitwardenの年間利用の請求へ支払いをしたので、こっちをどうするかを考える必要がありそうですが。
