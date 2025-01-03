=============================================
FastAPIでX-Forwarded-Hostを用いたリダイレクト
=============================================

.. post:: 2020-04-07
   :category: Tech
   :tags: Python,FastAPI,Gist,
   :redirect: blog/2020/fastapi-slash-tailed-redirection-by-forarded

ソースを見てみたい人向け
========================

https://gist.github.com/attakei/6b308a2a7949746a8027fc0258f1de1c

なにこれ
========

``FastAPI`` 用に作ったミドルウェアで、リクエスト時に ``X-Forwarded-Host`` ヘッダーが付与されていた場合に、
その値を `Host` ヘッダーに上書きするものです。
``FastAPI`` 用とはいっても、依存してるのは ``Starlette`` だけなので、 ``Starlette`` 派生なら普通に動くと思います。

何ができるの？
==============

``FastAPI`` が動いているサーバーのホスト名と、サービスのFQDNが違っているケースで、
いわゆる **Slashes redirection** が有効になっている際に、
そのリダイレクトもサービスのFQDNで行われるようになります。

コードを書いてみた背景とか
==========================

Firebase + Cloud Run の挙動
---------------------------

このサイトは現在実験を兼ねて、 ``Firebase Hosting`` + ``Cloud Run`` の組み合わせで動作していて、
一部のURLは バックエンド設定した ``Cloud Run`` サービスからレスポンスを返すようにしています。

.. mermaid:: request-flow.mmd
    :alt: Firebase+CloudRunのリクエストの流れ
    :caption: Firebase+CloudRunのリクエストの流れ
    :align: center

``Cloud Run`` はDockerコンテナを使って「サービス」を提供する機能のため、ホスト名を持っています。
``Firebase`` から ``Cloud Run`` への通信も最終的にはこのホスト名が使われ、
``Firebase`` のホスト名自体は、 ``X-Forwarded-Host`` ヘッダー経由で渡るようになっています。

.. mermaid:: browser-to-firebase.mmd
    :align: center
    :caption: ブラウザ-Firebase間のヘッダー(一部)

.. mermaid:: firebase-to-cloudrun.mmd
    :align: center
    :caption: Firebase-CloudRun間のヘッダー(一部)

FastAPIの Slashes redirection
-----------------------------

``FastAPI`` のルーティングは、 ``APIRouter`` クラスが担っています。
そして、 ``APIRouter`` のプロパティには ``redirect_slashes`` があります。

これは、 プロパティが ``True`` なら「末尾が ``/`` となるルーティング設定」がすでに存在する際に、
``/`` 末尾が足りないリクエストが来た場合に、 ``/`` スラッシュを付与したURLへリダイレクトさせる機能です。

.. mermaid:: redirect-slashes.mmd
    :align: center
    :caption: FastAPIとブラウザのやり取り例

このとき、内部ではリダイレクト先のURLをスキーマから全部構築した状態で、用意します。
そして、その時の参照状情報として ``Host`` ヘッダーを利用しています。

組み合わさるとどうなるか
------------------------

上記2点が組み合わさると、 Cloud Runの視点では ``Host`` ヘッダーはあくまで ``Cloud Run`` 自身のサービスFQDNとなるため、

**「Firebaseのホスト名でredirect-slashesの条件を満たすと、Cloud Runのホスト名のURLでリダイレクト指示を出す」**

という状況が発生してしまいます。

.. mermaid:: request-sequence.mmd
    :align: center
    :caption: 実際のリクエスト

「なんのためのFirebaseなのか」といった感じですね。

中身的には、こんな感じです。

.. literalinclude:: routing.py
    :language: python

どう対処したか
==============

https://gist.github.com/attakei/6b308a2a7949746a8027fc0258f1de1c

ミドルウェアを用意してリクエスト処理に割り込みを行い、
「 ``X-Forwarded-Host`` ヘッダーがあった時に限り、 ``Host`` ヘッダーの中身を上書きする」
ようにしました。

.. literalinclude:: middleware.py
    :language: python
    :lines: 8,22-
    :linenos:

弊害はあるか？
--------------

他に ``Host`` ヘッダを元に何かを識別しているケースがあると、もしかしたら想定外の挙動をするかもしれません。

ただ自分の場合だと、アプリケーションの中身自体は極力 ``Host`` ヘッダーに依存しないよう作っているので、
きっと害は無いと信じてます。

Links
=====

* https://github.com/tiangolo/fastapi/blob/0.54.0/fastapi/routing.py#L402
* https://github.com/encode/starlette/blob/master/starlette/routing.py#L454
* https://github.com/encode/starlette/blob/master/starlette/routing.py#L564
