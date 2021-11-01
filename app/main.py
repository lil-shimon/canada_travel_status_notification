import get_status
import line_notify

if __name__ == "__main__":
  status = get_status.get_status_handler()
  description = get_status.get_description_handler()
  message = status + "\n >> " + description
  line_notify.push_notify(message)
