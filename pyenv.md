# pyenv まとめ
pyenvはサーバ上で複数のバージョンのpythonを管理できるようにする。  
例えばユーザ1,2,3はpython2.7を使いたい、ユーザ4,5はpython3.5を使いたいといった場合に、それぞれが個別でインストールするよりも効率的に管理することができる。

具体的には  
* 複数のバージョンのPyhtonを`~./pyenv`以下に保存しておく。
  * Pathを随時切り替えることで使うバージョンを変更する。

といった感じ。

## `pyenv version` と`pyenv versions`
現在使用しているバージョンと利用可能なバージョンの表示
```shell-session
$ pyenv version
2.7.10 (set by /home/gocho/.python-version)
$ pyenv versions
  system
* 2.7.10 (set by /home/gocho/.python-version)
  3.4.4
```

## `pyenv install`
Pythonの新しいバージョンのインストールとインストール可能なバージョンの確認  
インストール先は`~/.pyenv/versions`以下
```shell-session
$ pyenv install -l
Available versions:
  2.1.3
  (以下略)
$ pyenv install 2.7.10
$ pyenv install 3.4.4
```

## `pyenv global`、`pyenv local`、`pyenv shell`
使用するPythonのバージョンの切り替え  
###`pyenv global`
デフォルトのpythonのバージョン変更。ユーザ全員のバージョンが変わる。(localやshellで設定している場合を除く)  
`~/.pyenv`の下にある`version`というファイルの中身が書き換わる
```shell-session
$ pyenv global 3.4.4
$ python -V
Python 3.4.4
```

###`pyenv local`
ユーザ個人のpythonのバージョン変更。他のユーザが使うバージョンは変わらない。  
カレントディレクトリに`.python-version`というファイルを生成(すでにある場合は中身を書き換える)  
`global`の設定より優先される。
```shell-session
$ pyenv local 2.7.10
$ python -V
Python 2.7.10
```

###`pyenv shell`
一時的なpythonのバージョン変更。現在のシェル上でのみ有効。ログアウトするとこの設定は消える。  
直接環境変数をsetしているらしい。
`global`、`local`の設定より優先される。
```shell-session
$ pyenv shell 3.4.4
$ python -V
Python 3.4.4
$ logout

$ python -V
Python 2.7.10
```
