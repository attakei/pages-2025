errbot-pomodoro-timerの修正メモ
===========================================

.. post:: 2017-06-11
   :category: Tech
   :tags: Python,OSS,Errbot,

公開しているErrbot用のプラグイン `errbot-pomodoro-timer <https://github.com/attakei/errbot-pomodoro-timer>`_ について、
Errbot 5.0.1で使用するときに読み込み失敗するエラーがあったので修正してました。

出てたエラー
------------

.. code-block:: console

   ❯ errbot -c demo.py
   (略)
   21:25:50 ERROR    yapsy                     Unable to create plugin object: ~~/errbot-pomodoro-timer/pomodoro
   Traceback (most recent call last):
     File "~/venv/lib/python3.6/site-packages/yapsy/PluginManager.py", line 512, in loadPlugins
       plugin_info.plugin_object = self.instanciateElement(element)
     File "~/venv/lib/python3.6/site-packages/errbot/plugin_manager.py", line 265, in instanciateElement
       return element(self.bot, name=self._current_pluginfo.name)
   TypeError: __init__() got an unexpected keyword argument 'name'
   (略)
   >>> !pomodoro start
   Command "pomodoro" not found.

何が悪いのか
------------

プラグインのロードに使っていると思われる、 **instanciateElement** が Errbot 5.0以降引数を2個取るようになっていた模様。

`4.3 におけるplugin_manager.py <https://github.com/errbotio/errbot/blob/4.3/errbot/plugin_manager.py#L250>`_

.. code-block:: python3

    def instanciateElement(self, element) -> BotPlugin:
        """Overrides the instanciation of plugins to inject the bot reference."""
        return element(self.bot)

`5.0 におけるplugin_manager.py <https://github.com/errbotio/errbot/blob/5.0/errbot/plugin_manager.py#L263>`_

.. code-block:: python3

    def instanciateElement(self, element) -> BotPlugin:
        """Overrides the instanciation of plugins to inject the bot reference."""
        return element(self.bot, name=self._current_pluginfo.name)

そして、 `うかつにも__init__をオーバライドしていた自分のプラグイン <https://github.com/attakei/errbot-pomodoro-timer/blob/d06d21468fb05d1daa1f95595db259c52af37fb4/pomodoro.py#L12>`_

.. code-block:: python3

    class Pomodoro(BotPlugin):
        WORK_MIN = 25
        REST_MIN = 5

        def __init__(self, bot):
            super().__init__(bot)
            self._runners = {}

直す
----

冷静に見返せば、 **__init__()** で追加でやろうとしていたのは別に **activate** でできるので、とっとと移植して終了。
