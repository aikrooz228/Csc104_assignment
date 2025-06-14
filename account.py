class Account:
    def __init__(self,balance,limit):
        self.balance=balance
        self.limit=limit


    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            print("New balance is:", self.balance)
        else:
            print("Insufficient Funds")

    def deposit(self,amount):
        if amount>=0:
                self.balance += amount
                print("New balance is:", self.balance)


