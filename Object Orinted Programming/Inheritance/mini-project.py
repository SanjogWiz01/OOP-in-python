class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}, Balance: {self.balance}")
        else:
            print("Insufficient balance")

class SavingAccount(Account):
    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest = interest

    def add_interest(self):
        self.balance += self.balance * self.interest / 100
        print(f"Interest added, New Balance: {self.balance}")

class CurrentAccount(Account):
    def __init__(self, name, balance, overdraft):
        super().__init__(name, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft:
            self.balance -= amount
            print(f"Withdrawn {amount}, Balance: {self.balance}")
        else:
            print("Exceeds overdraft limit")

s = SavingAccount("Sanjog", 1000, 5)
c = CurrentAccount("Anita", 500, 200)
s.add_interest()
c.withdraw(600)
s.deposit(200)
c.withdraw(200)