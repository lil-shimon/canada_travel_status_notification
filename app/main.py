import requests
from bs4 import BeautifulSoup

url = 'https://www.ca.emb-japan.go.jp/itpr_ja/Covid19_20200330.html'
res = requests.get(url)
print(res.text)