==============
Errcron: 0.4.4
==============

.. post:: 2017-11-12
   :category: Tech
   :tags: Python,OSS,Errbot,

自分用のbotを作り直してたときに、挙動の異常に気づいて修正しました。

`細かい情報はこちら <https://pypi.org/project/errcron/>`_

更新点について
==============

依存関係ライブラリの挙動変更対応のため、機能の追加や削除といった類ではないです。

* ``CronJob.is_runnable()`` の挙動を ``parse-crontab`` の仕様に対してゆるい対応を行う
* Travis-CIのテストターゲット設定が変だったので、正しくする

CronJob.is_runnable()の挙動修正
-------------------------------

これが本題です。

Errcronでは、crontab文字列の実行可能判定を `parse-crontab`_ を用いて行っています。
コードの中身的にはこんな感じ。
（self._crontabはparse-crontabのCrontabオブジェクトです）

.. code-block:: python

    def is_runnable(self, time):
        if self._crontab is not None:
            return self._crontab.test(time)
        return time.strftime(self.trigger_format) == self.trigger_time

``time`` の中身は基本的にErrbotのpollerの周期で呼ばれるため、何秒になるかはわかりません。
（一応、仕様として、30間隔でポーリングは動作し、0-29のときだけが対象です）

今まではこれで問題なく動いたのですが、先月の `parse-crontab`_ の更新時に
`「秒単位のcrontab」がサポートされるようになった <https://github.com/josiahcarlson/parse-crontab/issues/24>`_ らしく、
CronTabオブジェクト上では、秒の値が必ず0になってしまうようになりました。

上記の通り、Errbotのpollerは必ずしも毎分0秒と30秒に呼ばれるとは限らないため、これでは動作が保証できなくなります。
今回はこのときの判定処理を改修して、 **「判定時だけ、~~時xx分0秒とみなす」** という修正をしています。

.. code-block:: python

    def is_runnable(self, time):
        if self._crontab is not None:
            zero_time = time.replace(second=0)    # <= 秒だけ0にするdatetimeを作り
            return self._crontab.test(zero_time)  # <= timeでなく、zero_timeで判定
        return time.strftime(self.trigger_format) == self.trigger_time

Travis-CIの動作修正
-------------------

Travis-CI上ではtoxでテストを実行してるのですが、全部の実行環境をpython3.6にしてしまったらしく、
`それが何故かpy35のパターンのみ失敗するというよくわかってない現象 <https://travis-ci.org/attakei/errcron/builds/300904151>`_ で不備に気づきました。

とりあえず正したのですが、このブログ書きながら「Python2.7のテストが何処かに消えた」ということに気づきました。
（Errbot本体がpython2.xをすでにサポートしてないので別にいいのかもしれないのですが）

教訓
====

依存ライブラリには注意を払わないといけない

.. _parse-crontab: https://github.com/josiahcarlson/parse-crontab
