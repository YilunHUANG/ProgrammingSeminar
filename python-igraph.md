#python-igraph まとめ
igraphのホームページは[こちら](http://igraph.org/ "igraph")

windowsではインストールは少しめんどくさい。`pip`や`easy_install`が使えない。  
UNIX系はCのコンパイラがあれば`pip`でできるらしい。  
~~理由不明だが、研究室のサーバでできなかった(エラーコード : Could not download and compile the C core of igraph.)  
コンパイルができないっていわれた。~~

(2/16 追記)  
lxmlのビルドに必要なパッケージが不足していたらしい。`yum install libxslt-devel` でインストールした後、`pip`を使ってインストールできた。  
[参考](https://teratail.com/questions/4839 "【Python】pip install が出来ない件について！")


##インストール方法(windows)
* 別のライブラリ`wheel`をインストールする。
  * `pip install wheel` 
* [このサイト](http://www.lfd.uci.edu/~gohlke/pythonlibs/)から自分のPythonのversionにあったpython-igraphのwhlファイル(バイナリファイル)をダウンロードする。インストールにCコンパイラが必要でエラーとなるほかのライブラリもここで入手可能と思われる。
* ダウンロード後  `pip install "ファイル名".whl` でインストール

##python-igraph
* グラフに関する操作のライブラリ。PythonのほかにR,C++などでも利用可能。Pythonでは似たようなものに`networkx`がある。一般的にはRでigraphを、Pythonでnetworkxを利用しているらしい。igraphは中身はCで書かれていて、実行速度は速いらしい(時間があればnetworkxとpython-igraphで速度を比較してみたい)。python,igraphで検索しても日本語のサイトで充実しているのは少ないort  

##ソースコード例
* インポート
```py
import igraph
```

* グラフ作成  
引数の初期値は(n=None, edges=None, directed=None, graph_attrs=None, vertex_attrs=None, edge_attrs=None)  
```py
g0 = igraph.Graph()
g1 = igraph.Graph(10)
g2 = igraph.Graph([(0,1), (0,2), (1,2)])
g3 = igraph.Graph(10, [(0,1), (0,2), (1,2)])
```   

* 頂点、辺の追加  
```py
g.add_vertex()
g.add_vertices(10)
g.add_edge(0, 1)
g.add_edges([(0,1), (0,2), (1,2)])
```

* 頂点、辺の削除  
```py
g.delete_vertices(None)
g.delete_vertices([0,3,5])
g.delete_edges(None)
g.delete_edges([0,1,3])
g.delete_edges([(0,1), (0,2), (1,2)])
```
