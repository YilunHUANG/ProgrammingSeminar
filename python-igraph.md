# python-igraph まとめ
igraphのホームページは[こちら](http://igraph.org/ "igraph")

windowsではインストールは少しめんどくさい。`pip`や`easy_install`が使えない。  
UNIX系はCのコンパイラがあれば`pip`でできるらしい。  
~~理由不明だが、研究室のサーバでできなかった(エラーコード : Could not download and compile the C core of igraph.)  
コンパイルができないっていわれた。~~

(2/16 追記)  
lxmlのビルドに必要なパッケージが不足していたらしい。`yum install libxslt-devel` でインストールした後、`pip`を使ってインストールできた。  
[参考](https://teratail.com/questions/4839 "【Python】pip install が出来ない件について！")


## インストール方法(windows)
* 別のライブラリ`wheel`をインストールする。
  * `pip install wheel` 
* [このサイト](http://www.lfd.uci.edu/~gohlke/pythonlibs/)から自分のPythonのversionにあったpython-igraphのwhlファイル(バイナリファイル)をダウンロードする。ほかのライブラリもここで入手可。
* ダウンロード後  `pip install "ファイル名".whl` でインストール

## python-igraph
* グラフに関する操作のライブラリ。PythonのほかにR,C++などでも利用可能。Pythonでは似たようなものに`networkx`がある。一般的にはRでigraphを、Pythonでnetworkxを利用しているらしい。igraphは中身はCで書かれていて、実行速度は速いらしい(時間があればnetworkxとpython-igraphで速度を比較してみたい)。python,igraphで検索しても日本語のサイトで充実しているのは少ないort  
グラフの参照渡しになっているメソッドが多いので、変更後のグラフと変更前のグラフを後で比較したいときはあらかじめ`g1 = g.copy()`としてグラフのコピーをとる必要がある。

## ソースコード例
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

* グラフの確認  
```py
print g           #辺のリストも表示する
#出力例
"""
IGRAPH U--- 10 14 --
+ attr: id (v), label (v)
+ edges:
0--2 0--3 0--6 1--2 1--9 2--8 3--9 4--5 4--7 5--6 8--9 0--1 0--8 1--8
"""
igraph.summary(g) #辺のリストを省略
#出力例
"""
IGRAPH U--- 10 14 -- 
+ attr: id (v), label (v)
"""
```

* グラフの読み込み・書き込み  
グラフのデータのフォーマットはいくつかあるが拡張子から自動で適切なフォーマットで読み込む(書き込む)。
```py
# ファイルから読み込む
g = igraph.read("FileName")

# グラフをファイルに書き込む
igraph.write(g, "FileName")
```

* そのほか
```py
# グラフを有向(無向)グラフにする
directed_graph = g.as_directed() #引数なし(True) -> 無向辺は両方向の2辺になる。 引数False -> 無向辺はノード番号が小から大への向き
undirected_graph = g.as_undirected() #引数なし(True) -> 2方向の辺は1つの辺になる。 引数False -> 2方向の辺は2重辺のなる。

# グラフを単純グラフにする
g.simplify()

# 隣接頂点(辺)を返す
adjacent = g.adjacent(vertex)    #引数の頂点に隣接する辺のリストを返す。辺はid(記憶された順に0,1,2,...)で返される。
neighbors = g.neighbors(vertex)  #引数の頂点に隣接する頂点のリストを返す。頂点はid(記憶された順に0,1,2,...)で返される。
neighborhood = g.neighborhood(vertex, order = 1) #引数の頂点からorder以内のステップ数で辿り着ける頂点の集合(重みは考慮されないみたいです)
```
