from account import Account

class SavingAccount(Account):
    def __init__(self, balance):
        super().__init__(balance) 

    def withdraw(self, amount, limit):
        if amount < limit:
            super().withdraw(amount)
        else:
            print(f"Withdrawal limit exceeded. You can only withdraw up to {limit}.")

    def deposit(self, amount):
        if amount > 0:
            super().deposit(amount)


customer = SavingAccount(100)
customer.deposit(1000)
customer.withdraw(5000, 10000)
