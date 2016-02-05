#python-igraph まとめ
igraphのホームページは[こちら](http://igraph.org/ "igraph")

インストールは少しめんどくさい。windowsでは`pip`や`easy_install`が使えない。
UNIX系はCのコンパイラがあれば`pip`でできるらしい(詳しくはまだ分かりません)

##インストール方法(windows)
* 別のライブラリ`wheel`をインストールする。
  * `pip install wheel` でできる。
* [このサイト](http://www.lfd.uci.edu/~gohlke/pythonlibs/)から自分のPythonのversionにあったpython-igraphのwhlファイルをダウンロードする。
* `pip install "ファイル名".whl` でインストールできる

##Chainer特徴
* pythonでニューラルネットワークを簡単に記述できる。
* 各層をつなぐネットワークの関数、活性化関数、誤差関数があらかじめ用意されている。
* 最適化の手法も様々用意されている。
* 他のフレームワーク(Caffe, theano)に比べ、ネットワークの記述が短くてすむ。
* Caffeの学習済みモデルを使うこともできる(使い方はまだ勉強してないです…)

##注意するところ
Chainerでは型に関するエラーが1番多いと思われる。
* Chainerに組み込まれている関数を使うには `(変数名) = chainer.Variable(変換前変数)` を用いて、Chainer専用の型に変換する必要がある。
* 変換する前の変数はnumpyのndarray型にする必要がある。
* numpyのデフォルトはndarrayの64bit型だが32bit型である必要がある。
  * `x.astype(np.float32), t.astype(np.int32)` 
* 入力のndarrayはLinearに渡すときは(データの数,入力変数の数)の形にする。
  * `x_train = x_train.reshape(len(x_train), 1)`
* 入力をConvolution2Dに渡すときは画像を (nsample, channel, height, width) の4次元テンソルに変換
  * `X_train = x_train.reshape((len(x_train), 1, 28, 28))`
* 当然ながら各層の出力の数と次の層の入力の数が一致しているようなネットワークを書かないとエラーが起こる。

##ソースコード例

* 学習したモデルの保存
```py
import cPickle
cPickle.dump(model, open("FILENAME.pkl", "wb"), -1)
```
