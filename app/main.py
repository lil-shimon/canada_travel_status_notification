import get_status
import line_notify
import config

def push_notify_handler():
  """
  カナダ渡航状況が変更された時にLine通知する
  """
  status = get_status.get_handler(config.MessageType.STATUS.value)
  description = get_status.get_handler(config.MessageType.DESCRIPTION.value)
  message = status + "\n >> " + description if get_status.check_updated_status(status, config.MessageType.STATUS.value) or get_status.check_updated_status(description, config.MessageType.DESCRIPTION.value) else None
  if message:
    line_notify.push_notify(message)

if __name__ == "__main__":
  push_notify_handler()