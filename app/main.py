import get_status
import line_notify
from config import MessageType

def push_notify_handler():
  """
  カナダ渡航状況が変更された時にLine通知する
  """
  status = get_status.get_handler(MessageType.STATUS.value)
  description = get_status.get_handler(MessageType.DESCRIPTION.value)
  message = status + "\n >> " + description if get_status.check_updated_status(status, MessageType.STATUS.value) or get_status.check_updated_status(description, MessageType.DESCRIPTION.value) else None
  if message:
    line_notify.push_notify(message)

if __name__ == "__main__":
  push_notify_handler()