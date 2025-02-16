from notifypy import Notify
import time

notification = Notify()

def show_notification(title, message):
    notification.title = title
    notification.message = message
    notification.send()
