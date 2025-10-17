from notifier import Notifier
from sms_notifier import SMSNotifier
from email_notifier import EmailNotifier

class OrderProcessor:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def process_order(self, order_id: int, customer_contact: str):
        self.notifier.send(
            recipient=customer_contact,
            subject=f"Order {order_id} Confirmed",
            message="Thank you for your order!"
        )

if __name__ == "__main__":
    sms_notifier = SMSNotifier()
    email_notifier = EmailNotifier()

    order_processor_sms = OrderProcessor(sms_notifier)
    order_processor_email = OrderProcessor(email_notifier)

    order_processor_sms.process_order(123, "+1234567890")
    order_processor_email.process_order(456, "test@example.com")
