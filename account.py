class Account:
    def __init__(self,balance):
        self.balance=balance


    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


    def deposit(self,amount):
        self.balance +=amount