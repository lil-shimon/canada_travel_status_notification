import requests
import config

def push_notify(message):
  """
  push notification to line

  Parameters
  ----------
  message : str
    message to send
  
  Returns
  -------
  None
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