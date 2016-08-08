import requests

re = requests.get('http://www.zhihu.com')
print re.content