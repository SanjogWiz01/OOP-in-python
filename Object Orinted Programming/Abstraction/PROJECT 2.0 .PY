# Bank_Management_System.py
# Example of Data Abstraction in Python
# Internal account details are hidden from the user


class BankAccount:

    def __init__(self, name, account_number, balance):

        # Private data (hidden)
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance


    # Public method to deposit money
    def deposit(self, amount):

        if amount > 0:
            self.__balance = self.__balance + amount
            print("Money Deposited Successfully")
        else:
            print("Invalid Amount")


    # Public method to withdraw money
    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Money Withdrawn Successfully")
        else:
            print("Insufficient Balance")


    # Public method to check balance
    def check_balance(self):

        print("Current Balance =", self.__balance)


    # Public method to display account info
    def show_account(self):

        print("\nAccount Details")
        print("Name =", self.__name)
        print("Account Number =", self.__account_number)



# Main Program

name = input("Enter Name: ")
acc = input("Enter Account Number: ")
bal = int(input("Enter Initial Balance: "))

user1 = BankAccount(name, acc, bal)

while True:

    print("\n1 Deposit")
    print("2 Withdraw")
    print("3 Check Balance")
    print("4 Account Info")
    print("5 Exit") # making the condiotions that user can selects from them

    choice = input("Enter Choice: ")

    if choice == '1':

        amt = int(input("Enter Amount: "))
        user1.deposit(amt)

    elif choice == '2':

        amt = int(input("Enter Amount: "))
        user1.withdraw(amt)

    elif choice == '3':

        user1.check_balance()

    elif choice == '4':

        user1.show_account()

    elif choice == '5':

        print("Thank You")
        break

    else:

        print("Invalid Choice")