# Python Jupyter 編

## Overview

　[Jupyter notebook](http://jupyter.org/) とは，ブラウザベースのインタラクティブシェルのことである．Anaconda を使用している場合，標準でインストールされている．Python の他，R，Julia，Haskell，Ruby といった言語でも利用出来る．

## Settings

　サーバで起動した Jupyter notebook にクライアントからアクセスしたい場合，以下の手順を踏む必要がある．[公式のドキュメント](http://jupyter-notebook.readthedocs.io/en/latest/public_server.html)に詳しい記述がある．

　クライアントからアクセスするためのパスワードを設定する．

```
$ jupyter console
In [1]: from notebook.auth import passwd
In [2]: passwd()
Enter password:
Verify password:
Out[2]: 'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'
```

　Jupyter の設定ファイル `~/.jupyter/jupyter_notebook_config.py` を生成する．

```
$ jupyter notebook --generate-config
```

　`~/.jupyter/jupyter_notebook_config.py` を編集する．

```~/.jupyter/jupyter_notebook_config.py
# c.NotebookApp.certfile = '' # 99 行目．
c.NotebookApp.ip = '*' # 155 行目．
# c.NotebookApp.keyfile = '' # 174 行目．
# c.NotebookApp.notebook_dir = '' # 186 行目．
c.NotebookApp.open_browser = False # 192 行目．
c.NotebookApp.password = 'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed' # 201 行目．
c.NotebookApp.port = <port> # 204 行目．
```

　Jupyater notebook を起動する．

```
$ jupyter notebook
```

　全て終えると，クライアントのブラウザから `http://<host>:<port>/` にアクセスできる．
## Usage

主なショートカットキーを挙げる．

### Command mode (Bule)

- `Enter` Edit mode へ切替
- `m` マークダウンセルへ切替
- `y` コードセルヘ切替
- `a` 上にセルを追加
- `b` 下にセルを追加
- `k` 上のセルへ移動
- `j` 下のセルへ移動
- `Shift + k` 選択範囲を上へ拡張
- `Shift + j` 選択範囲を下へ拡張
- `Shift + m` 選択中のセルを結合
- `x` 選択中のセルを切取り
- `c` 選択中のセルをコピー
- `dd` 選択中のセルを削除
- `v` セルを貼り付け
- `Ctrl + Enter` 選択中のセルを実行
- `s` 内容を保存
- `00` カーネルを再起動
- `f` 単語を検索（置換）
- `l` 行番号を表示（非表示）
- `h` ショートカットキーを確認

### Edit mode (Green)

- `Esc` Command mode へ切替
- `Tab` インデント（補完）
- `Ctrl + Enter` 選択中のセルを実行