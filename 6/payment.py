from dataclasses import dataclass
from decimal import Decimal, InvalidOperation

# Custom exception for validation errors
class ValidationError(Exception):
    pass

# Custom exception for payment processing errors
class PaymentError(Exception):
    pass

@dataclass(frozen=True)
class PaymentResult:
    """
    Represents the result of a payment transaction.
    This is an immutable data class.
    """
    transaction_id: str
    amount: Decimal
    status: str

class PaymentValidator:
    """
    A validator for payment data.
    """
    @staticmethod
    def validate_amount(amount) -> Decimal:
        """
        Validates the payment amount.
        Fails fast if the amount is invalid.
        """
        try:
            decimal_amount = Decimal(str(amount))
            if decimal_amount <= 0:
                raise ValueError("Amount must be positive.")
            return decimal_amount
        except (InvalidOperation, ValueError) as e:
            raise ValidationError(f"Invalid amount: {e}") from e

class PaymentProcessor:
    """
    Processes payments with safe defaults and input validation.
    """
    def __init__(self, debug_mode: bool = False, max_retry: int = 3, timeout: int = 30):
        self.debug_mode = debug_mode
        self.max_retry = max_retry
        self.timeout = timeout
        if self.debug_mode:
            print("PaymentProcessor initialized in debug mode.")
            print(f"Max retries: {self.max_retry}, Timeout: {self.timeout}s")

    def process_payment(self, amount, account_number: str):
        """
        Processes a single payment.
        1. Validates the amount.
        2. (Simulates) sending the payment to a third-party service.
        """
        print(f"Processing payment of {amount} to {account_number}...")

        # 1. Fail Fast: Validate inputs immediately
        try:
            validated_amount = PaymentValidator.validate_amount(amount)
        except ValidationError as e:
            print(f"Payment failed: {e}")
            return None

        # (Simulated) 2. Attempt to send the payment
        try:
            print(f"Validated amount: {validated_amount}. Attempting to send payment...")
            # In a real application, this is where you would have the logic
            # to communicate with a payment gateway.
            # This could involve network requests and might fail.
            # For simulation, we'll just assume it's successful.
            transaction_id = "simulated_transaction_12345"
            status = "SUCCESS"
            print("Payment successful!")
            return PaymentResult(
                transaction_id=transaction_id,
                amount=validated_amount,
                status=status
            )
        except Exception as e:
            # Catch potential errors during payment communication
            raise PaymentError(f"Failed to process payment: {e}") from e