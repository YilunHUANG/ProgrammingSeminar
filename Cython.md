#Cython まとめ
PythonをC/C++に変換して実行速度を早くすることができる。
使うためにはC/C++のコンパイラが必要。

##インストール方法(windows)
* `pip install Cython` でインストール

##陥ったエラー
* コンパイル時 `Unable to find vcvarsall.bat` または `ValueError: [u’path’]` というエラーメッセージが出る。
 * Python2.7の場合  
1, [Python 2.7用のコンパクトなVC++ 9.0コンパイラ](https://www.microsoft.com/en-us/download/details.aspx?id=44266)をダウンロード  
2, 環境変数を変更してパスを通す。  
       * 変数名 : VS90COMNTOOLS, 値 : C:\Program Files (x86)\Microsoft Visual Studio 9.0\Common7\Tools\
  * Python3.*の場合

##ソースコード例
```py
import igraph
```

##
参考文献
* [http://www.regentechlog.com/2014/04/13/build-python-package-on-windows/#VC-2](http://www.regentechlog.com/2014/04/13/build-python-package-on-windows/#VC-2)
