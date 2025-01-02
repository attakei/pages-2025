========================================
Errbotの動向追跡(2018/06/17版)
========================================

.. post:: 2018-06-17
   :category: Tech
   :tags: Python,Errbot,OSS,

※定期的なアウトプットの訓練として、
ErrbotのGHプロジェクトの動向を雑にまとめてます。

Topics
======

``master`` ブランチから ``6.0`` ブランチが切り出されて、 **6.0.0-alpha が公開されました**

`変更点がまとまっています。 <https://github.com/errbotio/errbot/blob/master/CHANGES.rst>`_

最初に追いかけ始めた頃から比較的新しいPythonの機能を積極的に使いにいくスタイルなのですが、
今回の6.0から文字列関連の記述をf-stringへ全面的に移行し、Python3.5以下も完全に切り捨てているのが特徴です。

他には、

* StorageプラグインとBackendプラグインもYapsy非依存にして、install_requires除去 [#f1]_
* Webserverプラグインのコア部分を、bottle + rocket-errbot から Flask8へ変更

などが、ぱっと目に見える変更かなと思います。

影響度が高そうな人は、

* Python3.5までしか使えない環境の人
* Webhook機能を積極t系に使っている人

あたりでしょうか。

`「5.2系までにある機能のバグフィックスはバックポートする」と言っている <https://gitter.im/errbotio/errbot?at=5b1d3a11ddd61d08e544bb9f>`_ ので、しばらくはサポートされるとおもっていいと思います。

Commits
=======

* 6.0.0-alphaのCHANGELISTが更新されたのみです

Issues
======

* 更新なし

PRs
===

* 更新なし

.. [#f1] あれ、CfP...
