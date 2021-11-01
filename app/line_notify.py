import requests
import config

def push_notify(message):
  """ push_notify
      パラメータmessageをLINEで通知する
  """
  TOKEN = config.LINE_API
  headers = {"Authorization": f"Bearer {TOKEN}"}
  data = {
    "message": message
  }
  requests.post(
    "https://notify-api.line.me/api/notify",
    headers=headers,
    data=data
  )