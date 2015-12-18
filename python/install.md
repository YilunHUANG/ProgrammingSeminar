# Python の環境構築

Author: Keisuke Sugawara, Yu Ohori

Date: Nov. 20, 2015

OS: Windows, OS X

## Python のインストール

### Windows の場合

[www.python.org](http://www.python.org/downloads/windows) から  ` Windows x86 MSI installer` (32 bit) をダウンロード．今回は Python 3.4.3 をインストール．

Add python.exe to Path の項目で will be installed on local hard drive を選択すると Path が自動で設定される．

### OS X の場合

` $ brew install python3` で最新版をインストール． homebrew の詳細は省略．

## パッケージのインストール

### Windows の場合

`$ python -m pip install --upgrade pip` で pip を更新（管理者権限で実行）．

[sourceforge.net](http://sourceforge.net/projects/numpy/files/NumPy/) で `numpy-<version>-win32-superpack-python3.4.exe` をダウンロードした後，起動．現在の Numpy の最新版は 1.10.1 ．

[sourceforge.net](http://sourceforge.net/projects/scipy/files/scipy/) で  `scipy-<version>-win32-superpack-python3.4.exe` をダウンロードした後，起動．現在の Scipy の最新版は 0.16.1．

次の packages.txt を用意して残りのパッケージを `$ pip install -r packages.txt` で一括インストール．

```
appnope>=0.1.0
chainer>=1.4.1
cycler>=0.9.0
decorator>=4.0.4
filelock>=2.0.5
# gnureadline>=6.3.3
ipykernel>=4.1.1
ipython>=4.0.0
ipython-genutils>=0.1.0
Jinja2>=2.8
jsonschema>=2.5.1
jupyter-client>=4.1.1
jupyter-core>=4.0.6
MarkupSafe>=0.23
matplotlib>=1.5.0
mistune>=0.7.1
nbconvert>=4.1.0
nbformat>=4.0.1
networkx>=1.10
nose>=1.3.7
notebook>=4.0.6
numpy>=1.10.1
pandas>=0.17.0
path.py>=8.1.2
pexpect>=4.0.1
pickleshare>=0.5
protobuf>=2.6.1
ptyprocess>=0.5
Pygments>=2.0.2
pyparsing>=2.0.6
python-dateutil>=2.4.2
pytz>=2015.7
pyzmq>=15.0.0
scikit-learn>=0.17
scipy>=0.16.1
simplegeneric>=0.8.1
six>=1.10.0
terminado>=0.5
tornado>=4.3
traitlets>=4.0.0
wheel>=0.26.0
```

### OS X の場合

`$ pip3 install -r packages.txt` で一括インストール．
