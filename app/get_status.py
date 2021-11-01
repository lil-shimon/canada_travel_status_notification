import requests
from bs4 import BeautifulSoup

def get_status_handler():
  """ get_status_handler
      カナダ全土のレベルステータスを取得し、返す
  """
  url = 'https://www.ca.emb-japan.go.jp/itpr_ja/Covid19_20200330.html'
  res = requests.get(url)

  ## 文字化け直す
  res.encoding = res.apparent_encoding

  soup = BeautifulSoup(res.text, "html.parser")
  # elems = soup.find_all(href=re.compile("aly"))
  elems = soup.find_all('span')

  ## カナダ全土のレベルステータス
  canada_travel_status = elems[16].contents[0]
  return canada_travel_status
