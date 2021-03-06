import requests
from bs4 import BeautifulSoup
from config import (MessageType, STATUS, DESCRIPTION)
from services.search_service import check_included

URL = 'https://www.ca.emb-japan.go.jp/itpr_ja/Covid19_20200330.html'
INCLUDED = ["レベル", "完了した渡航者"]

def get_handler():
  """
  カナダ全土のレベルステータスなどを取得し、返す
  
  Returns
  -------
       : string
      現在の渡航状況や詳細など
  """
  res = requests.get(URL)

  ## 文字化け直す
  res.encoding = res.apparent_encoding

  soup = BeautifulSoup(res.text, "html.parser")
  elems = soup.find_all('span')

  lists = []
  for elem in elems:
    if check_included(elem.contents[0], INCLUDED):
      lists.append(elem.contents[0])
  return lists

def get_status_handler():
  """
  カナダ全土のレベルステータスを取得し、返す

  Returns
  -------
  canada_travel_status : string
      現在のカナダ渡航状況
  """
  soup = BeautifulSoup(res.text, "html.parser")
  # elems = soup.find_all(href=re.compile("aly"))
  elems = soup.find_all('span')

  ## カナダ全土のレベルステータス
  canada_travel_status = elems[16].contents[0]
  return canada_travel_status

def get_description_handler():
  """
  詳細を取得

  Returns
  -------
  description : string
      ステータス詳細
  """

  soup = BeautifulSoup(res.text, "html.parser")
  elems = soup.find_all('span')

  description = elems[18].contents[0]
  return description


def check_updated_status(message, type):
  """ 
  渡航ステータスが変化しているかを確認する

  Parameters
  ----------
  message : string
      比較対象となるメッセージ
  type : int
      比較対象となるメッセージのタイプ

  Returns
  -------
  True | False : bool
      比較して更新されているかどうか
  """
  prev = STATUS if type == MessageType.STATUS.value else DESCRIPTION
  return False if message == prev else True
