import get_status
import line_notify
from config import MessageType
from services.search_service import check_included

def push_notify_handler():
  """
  カナダ渡航状況が変更された時にLine通知する
  """
  message = get_status.get_handler()
  if message:
    line_notify.push_notify(message)

if __name__ == "__main__":
  push_notify_handler()
  