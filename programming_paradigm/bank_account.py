class BankAccount:
    def __init__(self, account_balance=0):
        # force to int so you never end up with .0
        self.account_balance = int(account_balance)

    def deposit(self, amount):
        self.account_balance += int(amount)

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= int(amount)
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
