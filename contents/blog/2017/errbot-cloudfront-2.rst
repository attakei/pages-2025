=========================
Update: errbot-cloudfront
=========================

.. post:: 2017-07-18
   :category: Tech
   :tags: Python,OSS,Errbot,


ちょっと前に少しだけ手直しした部分の日本語メモ

`プロジェクト自体はここにあります。 <https://github.com/attakei/errbot-cloudfront>`_

何を直したか？
================

Errbotには ``BOT_PREFIX`` というコンフィグがあり、
ここで指定した文字列から始まるメッセージのみをErrbotへの命令とみなします。
（デフォルトは ``!`` ）

``errbot-cloudfront`` ではいくつかの命令に対して「このときはこの命令を出しといて」
という案内を出しています。
最初のリリースでは、その命令内容がデフォルトの ``!`` から始まっていました。
今回の修正ではこれを ``BOT_PREFIX`` を参照するようになりました。

メモ
====

Errbotの ``config.py`` の中身をプラグインから確認するときは、
``self.bot_config`` で参照可能。


.. code-block:: python

    class MyPlugin(BotPlugin):
        @botcmd
        def check_prefix(self, msg, args):
            return self.bot_config.BOT_PREFIX  # <= Return '!'
