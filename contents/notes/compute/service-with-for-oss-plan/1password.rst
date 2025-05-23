=========================
1Password for Open Source
=========================

:追加: 2025/04/20

.. list-table::

   * - サービスのサイト
     - https://1password.com/
   * - OSSプランについてのページ
     - https://github.com/1Password/for-open-source

サービス自体の概要
==================

1Password自体は、AgileBits Inc.によって開発運営されているパスワードマネージャーSaaS。
暗号化された環境上にパスワード情報をはじめとした機密情報全般を管理して、
クライアント経由で利用できるようにするもの。

機密情報は前述の通りID/パスワードのペアに限られているわけではなく、例えば下記のようなもの扱える。

* APIキー
* SSHキー
* 単純な個人情報

補助機能としてランダムなパスワードを生成するツールなども備えており、
パスワード漏洩に対する防衛力を高めてくれる。

OSS向けプランについて
=====================

`1Password for Open Source <https://github.com/1Password/for-open-source>`_ と称して、
OSS活動をしている個人やチーム向けに、1PasswordのTeamプランを丸ごと提供してくれるというもの。
申し込み時点のプラン条件を維持できている限りは、無期限で利用できる。

利用条件（概要）
----------------

* そのOSSプロジェクト自体が、営利活動をしていないこと。
  GitHub SponsorsやOpen CollectiveのようなOSS固有のファンディングについては、「営利活動」の対象外となる。
* 単一のプロジェクトでの申請では、下記の条件を満たしていること。

  * OSSライセンスに基づいたものであること。
  * プロジェクトとしての活動が30日以上あること。
  * 申請者がそのプロジェクトのコアメンバーであること。

* チームとしての申請では、下記の条件を満たしていること。

  * OSSに関わる活動であること。
    関わっていればOSSそのものである必要はなく、ミートアップのようなコミュニティ活動向けにも使える。
  * 商業活動をしていないこと。


プラン適用の大まかな流れ
------------------------

#. OSSプランを利用出来るように、身なりを整える。
#. Teamプランで1Passwordのチームアカウントを作成しておく。
   Teamプランそのものは14日のトライアルもあるので、一度作成して使用感を試しておくと良い。
#. OSSプランのリポジトリで、Issue作成の形式で申請を出す。
#. プランが適用されるまで待つ。
   申請直後にBotによる判定が行われているが、従業員による判定で始めて有効になる。
   自分が申請したときは、Issue作成から1週間程度の時間が必要だった。

自分のケースでは、申請をして承認されるまでの間にトライアルの期間が過ぎてしまった。
特にクレジットカードの登録もしていなかったため少しだけ空白期間があったが、
特に問題なく継続利用できている。
