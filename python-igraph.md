#python-igraph まとめ
igraphのホームページは[こちら](http://igraph.org/ "igraph")

インストールは少しめんどくさい。windowsでは`pip`や`easy_install`が使えない。
UNIX系はCのコンパイラがあれば`pip`でできるらしい(理由不明だが研究室のサーバでできなかった)　　


##インストール方法(windows)
* 別のライブラリ`wheel`をインストールする。
  * `pip install wheel` 
* [このサイト](http://www.lfd.uci.edu/~gohlke/pythonlibs/)から自分のPythonのversionにあったpython-igraphのwhlファイルをダウンロードする。
* ダウンロード後  `pip install "ファイル名".whl` でインストール

##python-igraph
* グラフに関する操作のライブラリ。PythonのほかにR,C++などでも利用可能。Pythonでは似たようなものに`networkx`がある。一般的にはRでigraphを、Pythonでnetworkxを利用しているらしい。igraphは中身はCで書かれているみたいで実行速度は速いらしい。python,igraphで検索しても日本語のサイトで充実しているのは少ないort

##ソースコード例
```py
import igraph
```

