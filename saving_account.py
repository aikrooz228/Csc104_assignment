from account import Account

class SavingAccount(Account):
    def __init__(self, balance):
        super().__init__(balance) 

    def withdraw(self, amount):
        if amount < self.limit:
            super().withdraw(amount)
        else:
            print(f"Withdrawal limit exceeded. You can only withdraw up to {self.limit}.")

    def deposit(self, amount):
        if amount >0:
            super().deposit(amount)


