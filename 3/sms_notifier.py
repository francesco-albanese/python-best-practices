from notifier import Notifier

class SMSNotifier(Notifier):
    def send(self, recipient: str, subject: str, message: str):
        print(f"Sending SMS to {recipient}: {subject} - {message}")
