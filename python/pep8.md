# Python PEP 8 編

## PEPs

　可読性の高いコードを書くために，以下の 3 つに目を通すべきである．

- [PEP 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 20 The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- [PEP 257 Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

## Tools

### Installasion

　Anaconda を使用している場合，PEP 8 に従っているかどうかを確認する pep8 と，文法エラーを検出する pyflakes が標準でインストールされている．しかし，これらを別々に使うのは面倒なので，両方の内容をチェックする flake8 をインストールする．

```
$ conda install flake8
```


### Usage

　以下のコマンドを実行すると，コードに誤りがあるかどうかを確認することが出来る．

```
$ flake8 foo.py
```

　無視したいエラーコードがある場合は，`~/.config/flake8` にそれを記述する．

```~/.config/flake8
[flake8]
ignore = E221, E241, E272
max-line-length = 99
```