"""
AbstractBankingSystem
Demonstrates data abstraction using abstract classes, encapsulation, and polymorphism.
"""

from abc import ABC, abstractmethod

# Abstract base class for all accounts
class Account(ABC):
    def __init__(self, owner: str, balance: float):
        self._owner = owner
        self._balance = balance

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    def get_balance(self):
        return self._balance

    def get_owner(self):
        return self._owner

# Concrete class: SavingsAccount
class SavingsAccount(Account):
    def deposit(self, amount: float):
        self._balance += amount
        print(f"[Savings] Deposited ${amount}")

    def withdraw(self, amount: float):
        if amount <= self._balance:
            self._balance -= amount
            print(f"[Savings] Withdrew ${amount}")
        else:
            print("[Savings] Insufficient funds.")

# Concrete class: CurrentAccount
class CurrentAccount(Account):
    def __init__(self, owner: str, balance: float, overdraft_limit: float):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit

    def deposit(self, amount: float):
        self._balance += amount
        print(f"[Current] Deposited ${amount}")

    def withdraw(self, amount: float):
        if amount <= self._balance + self._overdraft_limit:
            self._balance -= amount
            print(f"[Current] Withdrew ${amount}")
        else:
            print("[Current] Overdraft limit exceeded.")

# Interface-like abstract class for transactions
class TransactionProcessor(ABC):
    @abstractmethod
    def process_transaction(self, account: Account, amount: float):
        pass

# Concrete transaction: Deposit
class DepositTransaction(TransactionProcessor):
    def process_transaction(self, account: Account, amount: float):
        account.deposit(amount)

# Concrete transaction: Withdrawal
class WithdrawalTransaction(TransactionProcessor):
    def process_transaction(self, account: Account, amount: float):
        account.withdraw(amount)

# Demo
if __name__ == "__main__":
    acc1 = SavingsAccount("SANJOG", 1000)
    acc2 = CurrentAccount("SANJOG", 500, overdraft_limit=300)

    deposit = DepositTransaction()
    withdraw = WithdrawalTransaction()

    deposit.process_transaction(acc1, 200)
    withdraw.process_transaction(acc1, 150)

    deposit.process_transaction(acc2, 100)
    withdraw.process_transaction(acc2, 800)

    print("Final Balances:")
    print(f"Savings: ${acc1.get_balance()}")
    print(f"Current: ${acc2.get_balance()}")