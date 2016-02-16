#python-igraph まとめ
igraphのホームページは[こちら](http://igraph.org/ "igraph")

windowsではインストールは少しめんどくさい。`pip`や`easy_install`が使えない。  
UNIX系はCのコンパイラがあれば`pip`でできるらしい。  
~~理由不明だが、研究室のサーバでできなかった(エラーコード : Could not download and compile the C core of igraph.)  
コンパイラができてないっていわれた。~~

(2/16 追記)  
lxmlのビルドに必要なパッケージが不足していたらしい。`yum install libxslt-devel` でいれたら成功した。  
[参考](https://teratail.com/questions/4839 "【Python】pip install が出来ない件について！")


##インストール方法(windows)
* 別のライブラリ`wheel`をインストールする。
  * `pip install wheel` 
* [このサイト](http://www.lfd.uci.edu/~gohlke/pythonlibs/)から自分のPythonのversionにあったpython-igraphのwhlファイル(バイナリファイル)をダウンロードする。インストールにCコンパイラが必要でエラーとなるほかのライブラリもここで入手可能と思われる。
* ダウンロード後  `pip install "ファイル名".whl` でインストール

##python-igraph
* グラフに関する操作のライブラリ。PythonのほかにR,C++などでも利用可能。Pythonでは似たようなものに`networkx`がある。一般的にはRでigraphを、Pythonでnetworkxを利用しているらしい。igraphは中身はCで書かれているみたいで実行速度は速いらしい。python,igraphで検索しても日本語のサイトで充実しているのは少ないort

##ソースコード例
```py
import igraph
```

