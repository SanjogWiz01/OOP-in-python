

from abc import ABC, abstractmethod

# Abstract class
class ATM(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass


# Derived class
class MyATM(ATM):

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw Successful")
            print("Remaining Balance =", self.balance)
        else:
            print("Insufficient Balance")


# Main Program
a = MyATM(1000)
a.withdraw(300)