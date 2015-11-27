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
model = chainer.FunctionSet(
                          l1 = F.Linear(1,unit),     #入力層ー隠れ層
                          l2 = F.Linear(unit,1)      #隠れ層ー出力層
                          )
```

```py
model = chainer.FunctionSet(
                            conv1 = F.Convolution2D(1, 20, ksize=5),
                            conv2 = F.Convolution2D(20, 50, ksize=5),
                            l1 = F.Linear(800, 500),
                            l2 = F.Linear(500, 10)
                            )
```

* 順伝播
```py
def forward(x_train, t_train):
    x, t = chainer.Variable(x_train), chainer.Variable(t_train)      #訓練データをchainerで使える型に変換
    h1 = F.tanh(model.l1(x))          #tanh関数
    #h1 = F.sigmoid(model.l1(x))       #sigmoid関数
    #h1 = F.relu(model.l1(x))          #relu関数
    y = model.l2(h1)
    loss = F.mean_squared_error(y, t)
    return loss, y          #平均2乗誤差と出力を返す
```

```py
def forward(x_data, y_data, train=True):
    x, t = chainer.Variable(x_data), chainer.Variable(y_data)
    #1層目の畳み込みの後にプーリング層
    h1 = F.max_pooling_2d(F.relu(model.conv1(x)), 2)
    #2層目の畳み込みの後にプーリング層
    h2 = F.max_pooling_2d(F.relu(model.conv2(h1)), 2)
    #3層目の出力
    h3 = F.dropout(F.relu(model.l1(h2)), train=train)
    #yの出力
    y = model.l2(h3)

    # 訓練時とテスト時で返す値を変える
    if train:
        # 訓練時は損失を返す
        # 多値分類なのでクロスエントロピーを使う
        loss = F.softmax_cross_entropy(y, t)
        return loss
    else:
        # テスト時は精度を返す
        acc = F.accuracy(y, t)
        return acc
```

* 重みの更新方法の記述
```py
opt = optimizers.SGD()      #重みの更新は勾配降下法を用いる。デフォルトの学習率はlr=0.01
opt.setup(model)
```

```py
# Optimizerをセット
optimizer = optimizers.Adam()   #重み更新にAdamという手法を用いる。
optimizer.setup(model)
```

* 学習

```py
opt.zero_grads()    #勾配初期化
loss = forward(x_train, t_train)    #順伝播から誤差を計算
loss.backward()   #誤差を逆伝播
opt.update()    #重みの更新
```
