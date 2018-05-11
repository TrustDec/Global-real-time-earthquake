import requests
res = requests.get("http://news.sina.com.cn/china/")
print(res.encoding)