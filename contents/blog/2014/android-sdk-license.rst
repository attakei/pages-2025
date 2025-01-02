===================================================
Android SDK LicenseとJavaのファイルエンコーディング
===================================================

.. post:: 2014-11-22
   :category: Tech
   :tags: OSS,Android,エンコーディング,Kivy,Python,

限定条件下でははるものの、日本語環境がまるまるを満たしている気配がするので、ちゃんとエントリーにしてみる。

元々は、`Kivy <http://kivy.org/>`_ の自分用テンプレートを作っていた際に、
`buildozer <https://github.com/kivy/buildozer>`_ を使っていた時にビルドが途中で止まってしまった事象を解消する際に見つけたもの。

限定条件下って
==============

* java実行時のファイルエンコーディングを全く指定していない。もしくは指定しているがUTF-8ではない。
* 作ったプログラムの処理過程で、Android SDKのライセンス内容を取り扱う

発生した事象
============

何が起きた
----------

buildozerはkivyアプリのAndroid/iOSビルドを手早く行えるようにするためのツールで、
Androidビルド時には自動的にant,SDK,NDKをダウンロードセットアップする仕組みがある。

で、SDKのインストール後にビルドツールなどをダウンロードしようとするのだが、これが確実にコケる。
( `参照 <https://groups.google.com/forum/#!topic/kivy-users/F34ZYtjgLKU>`_ )

↓こんな感じ

.. code-block::

   $ buildozer android debug
   (中略)
   (ライセンス)
   (中略)
   UnicodeDecodeError: 'utf8' codec can't decode byte 0x81 in position 760: invalid continuation byte

どうしてこうなった
------------------

上の通り、Android SDK License Agreementの表示途中で止まってる。そして、出てきた例外がUnicodeDecodeError。

ということで、Unicode表現でない何かを表示しようとしてコケたと推測。

改めて表示されていると思われる `Licenseの大元 <http://dl-ssl.google.com/android/repository/addon.xml>`_ にたどってみると、
なんか全角アポストロフィが1個混ざってる。

そして、`この辺り <http://blog.lidalia.org.uk/2011/04/setting-default-java-file-encoding-to.html>`_ を見ていくとわかるが、
デフォルトではjava実行時のファイルエンコーディングがUTF-8とは限らない。

さらに、pythonはUnicodeでデコードしようとする。

結論
----

#. buildozerが内部で **android debug** を実行しようとしたが
#. **javaのファイルエンコーディングを指定していなかった** ために、デフォルトの値が採用され
#. **デフォルトエンコーディングがUTF-8ではない** ことから、別の文字コードで出力されてしまい
#. buildozer自体はunicode文字列として処理しようとするが、*UTF-8でないので当然ながら処理に失敗し*
#. **UnicodeDecodeErrorが飛ぶ**

ということらしい。

しかたがないのでプルリク作った
==============================

https://github.com/kivy/buildozer/pull/155

「修正は可能な限りシンプルに」を心がけて、android update 周りのみにファイルエンコーディングをセットする対応。
一応、挙動を簡単に調べてJAVA_TOOL_OPTIONSはちゃんと継承＆上書きするように。

ちなみに、修正コードを書くのに2時間強、コミットログの手直しに1時間、プルリクの文章に4時間かかった（印象）

プルリクは日本語の概要を書いてからGoogle翻訳に相談しつつ書いたのだけれど、日本語の原文がこちら

.. code::

   現在のバージョンのbulldozerでは、”buildozer android build”のコマンドがパッケージ更新の段階で失敗します。
   出力された例外を調べると、次のことがわかりました。
   ・現在のAndroid-SDKのライセンスの内容に、非ASCIIな文字が含まれていること
   ・java実行時に、ファイルエンコーディングがUTF-8ではないことが有ること
   ・エンコーディングがUTF-8ではない環境下で、ライセンスを表示しようとすると、非ASCII文字のデコードに失敗して例外が発生すること

   上記の現象を解消するために、改修を行いました。


エンジニアとして、初めてgithub上でプルリクエストを投げて、割と素早くマージしてもらえたので記念にエントリー化。

おまけ
======

なお、その過程で「Android build-toolの新規インストールができない上に、更新分のインストールもできない」という結構な不備があったので、
`別途プルリク <https://github.com/kivy/buildozer/pull/156>`_ を出している。まだマージされていない。
