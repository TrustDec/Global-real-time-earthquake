import requests
res = requests.get("http://www.ceic.ac.cn/ajax/speedsearch?num=6&&page=1")
res.encoding = 'utf-8';
print(res.text)