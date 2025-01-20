class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account balance."""
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        self._account_balance += amount

    def withdraw(self, amount):
        """Withdraw the specified amount if funds are sufficient."""
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")
