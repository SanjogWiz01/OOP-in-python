class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

payments = [CreditCard(), UPI()]
for p in payments:
    p.pay(500)
