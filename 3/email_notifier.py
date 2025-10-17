from notifier import Notifier

class EmailNotifier(Notifier):
    def send(self, recipient: str, subject: str, message: str):
        print(f"Sending Email to {recipient}: {subject} - {message}")
