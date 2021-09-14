# bank account model with support for deposit and withdraw operation

class BankAccount:
    def __init__(self):
        self.balance = 0
        print(f"Your current  balance is {self.balance}")

    def witdraw(self, amount):
        self.balance-=amount
        print(f"Your withdrawl amount is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Your deposited amount is {self.balance}")


a = BankAccount()
a.deposit(1000)
a.witdraw(500)