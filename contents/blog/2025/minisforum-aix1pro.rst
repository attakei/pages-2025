Minisforum AI X1 Pro を買った
=============================

.. post:: 2025-08-13
   :category: Tech
   :tags: Python,PyCon,PyConJP

.. oembed:: https://bsky.app/profile/attakei.dev/post/3lw6kg5mvik27

ずっと使っていたNUC11（GPU付き）がいきなり沈黙したので、急遽購入した。

96GB+2TBのモデルを購入したのだが、スペック的には全方面で向上してる。
動画再生とVSCodeぐらいではほとんど音がしなくなったので、かなり快適になった。

物理GPUが消滅したが、自分の用途では必須級の出番がないので問題なさそう。

細かい使用感などは :doc:`ノート側 </notes/gadget/minisforum-aix1-pro>` に書こうと思ってる。

OSどうするか問題
----------------

NUC11ではArch Linux + Cinnamonを使っていたのだけれど、暫くの間はインストールされているWindows 11 Proで過ごそうかなと思ってる。

* 旧環境のGUI周りでちょっとした困りごとがあって、Windowsだとほぼ確実に解消できる。 [#]_
* WSLのオフィシャルOSにArch Linuxがあるので、今だとクリーンなWSLが意外と使えそう。
* 初動の要求メモリーが大きくなるが、96GB搭載なので富豪戦略を取れる。

.. [#] 多分あれこれ調べれば解消できるんだけど、このほうが楽なので良しとしている。

ファンレス系でDDR5のSO-DIMMを挿せるベアボーンを見つけたら、Lemur 12を移植してLinux復帰しようかなと。
