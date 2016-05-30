# Linux Linuxbrew 編


## Overview

　[Linuxbrew](http://linuxbrew.sh/) とは，OS X の [Homewbrew](http://brew.sh/) を基にして作られたパッケージマネージャである．yum や apt-get と比べて，最新バージョンのパッケージを，管理者権限を要することなくインストールすることが出来る．

## Installation

　以下の手順でインストールできる．

```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/linuxbrew/go/install)"
$ echo 'export PATH="$HOME/.linuxbrew/bin:$PATH"' >> ~/.bashrc
$ echo 'export MANPATH="$HOME/.linuxbrew/share/man:$MANPATH"' >> ~/.bashrc
$ echo 'export INFOPATH="$HOME/.linuxbrew/share/info:$INFOPATH"' >> ~/.bashrc
$ source ~/.bashrc
```

## Usage

　使用方法は Homebrew と基本的に同じである．

- パッケージを検索

```
$ brew search <package>
```

- パッケージをインストール

```
$ brew install <package>
```

- パッケージをアンインストール

```
$ brew uninstall <package>
```

- インストールしたパッケージの一覧を表示

```
$ brew list
```

　手元にインストールしたパッケージを，そのまま他の環境に移したいときに便利なのが `Brewfile` である．以下のコマンドを実行すると，カレントディレクトリに `Brewfile` が生成される．

```
$ brew brewdle dump
```

　生成した `Brewfile` を，パッケージをインストールしたい環境まで持っていき，次のコマンドを実行する．

```
$ brew brewdle
```
