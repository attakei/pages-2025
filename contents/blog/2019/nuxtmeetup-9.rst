========================
NuxtMeetUp#9聞きに行った
========================

.. post:: 2019-08-26
   :category: Tech
   :tags: Nuxt.js,Vue.js,技術イベント,

「NuxtMeetUp#9オールスター」 に行ってLTを聞いたので、その感想を雑多にまとめています。

概要
====

https://nuxt-meetup.connpass.com/event/135514/

目的
====

* Nuxt.jsの技術トピックの収集
* 上記を踏まえた、実用的な手法などの更新

感想
====

特に自己領域に近いもののみ抜粋しています。

* By LINE

  * https://speakerdeck.com/keitakn/nuxt-dot-js-and-testcode
  * Docker の ``Multi stage build`` の話。2年以上前からあるのに、全然目につかなかった
  * 便利な機能なのは間違いないんだけど、やっぱりI/Oが鬼門っぽい

* By エス・エム・エス

  * https://speakerdeck.com/keitakn/nuxt-dot-js-and-testcode
  * Nuxtベースのアプリケーションにおける、テストコード戦略の話
  * テスト対象の定め方を、テストの目的を前提に時間比で丁寧に解説されていたと思う
  * いくつか使ったことのないライブラリを知られたのは大きい

* By Merpay

  * https://speakerdeck.com/tanakaworld/split-a-nuxt-microservice-to-3-microservices
  * プロダクトチーム分離を契機に、サービスコードを分割していた話
  * 単一ドメイン内でのサービス分割を行い、パスに応じてAPI Gatewayが振り分ける形式
  * ちゃんとしたマイクロサービスアーキテクチャを土台に、きちんと戦略を立てて分割している感じがする
  * 共通部分だけでなく、その他も単一のブロックに分けるのは、まぁアリなのかなという感想

* By ROXX

  * https://slides.com/ushironoko/nuxt-function-api/#/
  * 関数ベースでコンポーネントを定義できる機能
  * 紹介された使われ方を見る限り、処理の分割（特に依存/非依存）なんかのときのアプローチとして選択肢になりそう
  * ただ、直感のまま使えるようになるのはまだ先っぽい
