# 04_private_attributes.py

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner        # private
        self.__balance = balance    # private

    def show_balance(self):
        print(f"Account holder: {self.__owner}, Balance: {self.__balance}")

account = BankAccount("Sanjog", 10000)
account.show_balance()  # ✅ Accessing via public method....................................
   # ........................
