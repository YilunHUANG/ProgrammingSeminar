# Python anyenv 編

## Overview

### Python

　データ分析の現場で，R と並んで最もよく採用されている言語．

#### pip

　Python 標準のパッケージマネージャ．

### Anaconda

　Python 本体に加えて，下記のようなデータ分析で利用される主要なパッケージを一括してインストールしたもの．

- Cython
- IPython
- Jupyter
- matplotlib
- NetworkX
- NLTK
- Numpy
- Pandas
- pyparsing
- scikit-learn
- Scipy
- SymPy

#### conda

　Anaconda が提供するパッケージマネージャ．
### pyenv

　rbenv を基にして作られた Python のバージョンマネージャ．

### anyenv

　様々な言語のバージョンマネージャを一括で管理できるようにしたもの．現在，次の言語に対応している．

- Renv (R)
- crenv (Crystal)
- denv (D)
- erlenv (Erlang)
- exenv (Elixir)
- goenv (Go)
- hsenv (Haskell)
- jenv (Java)
- luaenv (Lua)
- ndenv (Node.js)
- nenv (Node.js)
- nodenv (Node.js)
- phpenv (PHP)
- plenv (Perl)
- pyenv (Python)
- rbenv (Ruby)
- sbtenv (Scala)
- scalaenv (Scala)
- swiftenv (Swift)

## Installation

　anyenv をインストールする．

```
$ git clone https://github.com/riywo/anyenv ~/.anyenv
$ echo 'export ANYENV_ROOT="$HOME/.anyenv"'
$ echo 'export PATH="$ANYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(anyenv init -)"' >> ~/.bashrc
$ exec $SHELL -l
```

　pyenv とそのプラグインである pyenv-pip-rehash インストールする．

```
$ anyenv install pyenv
$ echo $SHELL -l
$ git clone https://github.com/yyuu/pyenv-pip-rehash.git $(pyenv root)/plugins/pyenv-pip-rehash
```

　Anaconda をインストールする．

```
$ pyenv install anaconda3-4.0.0
```

　使用する Python のバージョンを切替える．念のため，アップデートも同時に行う．

```
$ pyenv global anaconda3-4.0.0
$ conda update conda
$ conda update anaconda
$ conda update --all
$ pip install --upgrade pip
```

　インストールしたバージョンは次のコマンドで確認出来る．

```
$ pyenv versions
```