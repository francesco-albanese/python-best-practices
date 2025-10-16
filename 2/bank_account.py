from datetime import datetime
from typing import List

class Transaction:
    def __init__(self, amount: float, transaction_type: str, description: str):
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
        self.timestamp = datetime.now()

    def __str__(self) -> str:
        return (f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type}: "
                f"${self.amount:.2f} - {self.description}")

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._owner = owner
        self._balance = initial_balance
        self._transactions: List[Transaction] = []
        if initial_balance > 0:
            self._add_transaction(initial_balance, "DEPOSIT", "Initial deposit")

    def deposit(self, amount: float, description: str) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._add_transaction(amount, "DEPOSIT", description)
        return self._balance

    def withdraw(self, amount: float, description: str) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._add_transaction(amount, "WITHDRAWAL", description)
        return self._balance

    def get_balance(self) -> float:
        return self._balance

    def get_statement(self) -> List[str]:
        return [str(tx) for tx in self._transactions]

    def _add_transaction(self, amount: float, trans_type: str, description: str) -> None:
        transaction = Transaction(amount, trans_type, description)
        self._transactions.append(transaction)

    def __str__(self) -> str:
        return f"BankAccount(owner='{self._owner}', balance=${self._balance:.2f})"

if __name__ == "__main__":
    # Create a new bank account
    my_account = BankAccount("John Doe", 1000.0)
    print(my_account)

    # Make a deposit
    my_account.deposit(500.0, "Paycheck")
    print(f"Balance after deposit: ${my_account.get_balance():.2f}")

    # Make a withdrawal
    my_account.withdraw(200.0, "Groceries")
    print(f"Balance after withdrawal: ${my_account.get_balance():.2f}")

    # Get the account statement
    statement = my_account.get_statement()
    print("\n--- Account Statement ---")
    for tx_str in statement:
        print(tx_str)
    print("--- End of Statement ---")
