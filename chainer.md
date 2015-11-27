#Chainerまとめ

##Chainer特徴
* pythonでニューラルネットワークを簡単に記述できる。
* 各層をつなぐネットワークの関数、活性化関数、誤差関数があらかじめ用意されている。
* 最適化の手法も様々用意されている。
* 他のフレームワーク(Caffe, theano)に比べ、ネットワークの記述が短くてすむ。

##ソースコード例
* NNの記述

```py
unit=3
model=chainer.FunctionSet(
                          l1=F.Linear(1,unit),     #入力層ー隠れ層
                          l2=F.Linear(unit,1)      #隠れ層ー出力層
                          )
```

```py
model = chainer.FunctionSet(
                            conv1=F.Convolution2D(1, 20, ksize=5),
                            conv2=F.Convolution2D(20, 50, ksize=5),
                            l1=F.Linear(800, 500),
                            l2=F.Linear(500, 10)
                            )
```

* 順伝播
```py
def forward(x_train, t_train):
    x, t =chainer.Variable(x_train), chainer.Variable(t_train)      #訓練データをchainerで使える型に変換
    h1=F.tanh(model.l1(x))          #tanh関数
    #h1=F.sigmoid(model.l1(x))       #sigmoid関数
    #h1=F.relu(model.l1(x))          #relu関数
    y=model.l2(h1)
    loss = F.mean_squared_error(y, t)
    return loss, y          #平均2乗誤差と出力を返す
```
