import get_status
import line_notify

if __name__ == "__main__":
  status = get_status.get_status_handler()
  line_notify.push_notify(status)
