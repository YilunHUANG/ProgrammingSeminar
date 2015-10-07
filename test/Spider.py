import urllib.request

__author__ = 'Alan HUANG'

url = "http://www.google.co.jp"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)
