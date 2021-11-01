import requests
from bs4 import BeautifulSoup

def get_status_handler():
  url = 'https://www.ca.emb-japan.go.jp/itpr_ja/Covid19_20200330.html'
  res = requests.get(url)

  ## 文字化け直す
  res.encoding = res.apparent_encoding

  soup = BeautifulSoup(res.text, "html.parser")
  # elems = soup.find_all(href=re.compile("aly"))
  elems = soup.find_all('span')

  ## カナダ全土のレベルステータス
  canada_travel_status = elems[16].contents[0]
  print(canada_travel_status)

