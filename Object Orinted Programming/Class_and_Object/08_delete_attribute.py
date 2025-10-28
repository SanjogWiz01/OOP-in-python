class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

c1 = Car("Tesla", 100000)
c1.price = 90000  # update
print(c1.price)

del c1.price  # delete
print(hasattr(c1, 'price'))  # False
print(c1.brand)
print(c1.price)  # This will raise an AttributeError since price has been deleted