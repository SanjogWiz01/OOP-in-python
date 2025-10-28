

class Laptop:
    def __init__(self, brand, price):
        self._brand = brand
        self.__price = price

    def info(self):
        print(f"Brand: {self._brand}, Price: {self.__price}")

l = Laptop("Dell", 90000)
l.info()
# Accessing the private attribute directly will raise an AttributeError
# print(l.__price)  # ❌ This will raise an error