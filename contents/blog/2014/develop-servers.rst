Redmine + GitLab + Jenkins = 重い
=================================

.. post:: 2014-10-24
   :category: Tech
   :tags: Ruby,GitLab,Jenkins,

ほとんどタイトルで言いたいことをいい尽くした。

MSDNについてくるクレジットを利用して、Redmine, GitLab, JenkinsをWindows Azureの1台のVMにのせているのだが、
クレジット上限を考慮してA1にしていると、やっぱりメモリが不足気味な模様。

で、調べると最近のクラウドサーバの類でよくあるイメージと同じく、AzureのVMにもスワップが初期で割り当てられていない。

普通の手段でスワップ出すのもありなのだが調べた際に便利だったページが有ったので、URLだけ貼り付けておく。

http://blogs.technet.com/b/ksasaki/archive/2013/06/21/linux.aspx

感謝感謝
