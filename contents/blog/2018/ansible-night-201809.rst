Ansible Night in Tokyo 2018.09
==============================

.. post:: 2018-09-25
   :category: Tech
   :tags: Ansible,GitLab,

年末以来の参加。
今回はブロガー枠ですが、すみません遅刻しました。

テーマは、「GitLab」と「インフラCI」

GitLab で実現する Ansible コードの管理
--------------------------------------

（このトークの途中から参加）

GitLabパートナーでもあるクリエーションラインの荒井さん。

大半を聞けてないのだけれど、GitLabはCI/CDを自前で持ってくれているおかけで、
簡単なプロジェクト管理・ソースコード管理・デプロイと検証を一括で扱えて便利です。

オンプレ環境内にGitLab-CEを用意すれば、かなり自由にできるのでAnsibleコード以外にも
大量なユースケースをイメージできるので、一度触ってみてほしいかなと思う。

※途中で、「ブランチ」を「仮想空間」と表現していたのが記憶に残ってる

インフラCI実践ガイド 〜Ansible x GitLab による継続的改善例 〜 自動化の正しさの検証を自動化するには
--------------------------------------------------------------------------------------------------

「インフラCI実践ガイド」の著者でもある、レッドハット中島さんの発表。

ITインフラの効率化にあたり三位一体として考るべきなのが、

* 自動化
* 標準化
* プロセスの改善

今回はこのうち、「自動化」を主題にした話。

Playbookやロールなどが、様々な要因による変化などで動くのかが怪しくなるのはあったりするので、
いかにして正当性の担保をできるかは確かに課題になってそう。

実例としてサンプルのGitLab-CI/CDのパイプラインが紹介されていたけど、
単純なPlaybookの文法チェックやテストだけでなく、
デプロイ後の性能テストが含まれていた。

「『あるべき形』のイメージ」と「『CI』のできること」をきちんと把握することで、
自動化の幅が大きく変わっていくというのがよくわかるサンプルだった。

LTあれこれ
----------

まとめつつ、感想を

* `Ansible container in the kubernetes <https://speakerdeck.com/nnao45/ansible-container-in-the-kubernetes>`_
* `Ansibleの学習環境をvSphereで作ってるお話 <https://speakerdeck.com/skyjoker/ansiblefalsexue-xi-huan-jing-wovspheredezuo-tuteruohua>`_
* `ElasticBeanstalk で Ansible を使っている話 <https://www.slideshare.net/laughk/elasticbeanstalk-ansible>`_
* `マイベストVariables設定場所（異論、反論Wellcome！） <https://www.slideshare.net/ssuser1f3c12/ansiblejpbestvariablesplace>`_
* `Ansible deploys Istio on kubenetes environment <https://www.slideshare.net/ssuserd394af/ansible-deploys-istio-on-kubenetes-environment>`_
* `Create Amazon AMI by Packer w/z Ansible provisioner <https://docs.google.com/presentation/d/1yVjHN_35xPih3X3tlXgwpmxftLlCP8raC-i-1k5KJLc/edit#slide=id.p>`_

「Ansibleを〇〇な環境で使う」が多かった。

このあたり、Ansibleの標準添付モジュールの数が非常に多いことや、
割とちょっと頑張れば自分でモジュールを書くことが可能という利点が効いているなと言うのがポジティブな感想。

一方で、LTの最中でもぼんやり出てたように「これ、ここまでは使わなそう」な領域も間違いなく多いと思う。
個人的には、リソースの基本構成（サーバーならミドルウェアとその設定周り）より下までをAnsible担当領域にして、
その上位レイヤーで動作しているものは基本的に専門のツールで十分かなと思ってる。
（KubernetesをAnsibleでハンドリングする気には、自分もあまりなれない）

その他
------

* 水筒もらいました。保温能力が高いので、夏冬どちらでも重宝しそうな予感

  * 黒背景に黒い方のAnsibleロゴだったので完全にステルスだけど、良かったんだろうか

* Ansible飯に参加しました

  * コミュ障というよりこじらせた人見知りだけど、単純に人のちょっと深い話を隣で聞くのが好きだったりします
  * たまにちょっとしたきっかけで、自分側から話を広げられたりすると、ちょっとやったってなるのはお約束
  * 最終的に帰り道にて、何故かテキストサイト全盛期の話題で盛り上がるという

* サテライト会場とライブストリーミング

  * TwitterのTLでもライブストリームほしいという意見が出てましたね
  * 個人的には賛成だけど、コスト的にどういう負荷がかかるのかがちょっと気になりました

* 人のトークセッションを聞くと喋りたくなる件

  * 「AnsibleでのPCセットアップ管理」「Galaxyデビュー」とか需要あるかな？
