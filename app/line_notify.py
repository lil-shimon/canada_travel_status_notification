import requests
import config

def push_notify():
  TOKEN = config.LINE_API
  headers = {"Authorization": f"Bearer {TOKEN}"}
  data = {
    "message": "test"
  }
  requests.post(
    "https://notify-api.line.me/api/notify",
    headers=headers,
    data=data
  )