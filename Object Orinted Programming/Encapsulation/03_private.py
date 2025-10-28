class cat:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):  # public method to access private attribute
        return self.__name

    def get_age(self):   # public method to access private attribute
        return self.__age

    def set_age(self, age):  # public method to modify private attribute
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")
c1 = cat("Whiskers", 3)
print(c1.get_name())  # Accessing private attribute via public method
print(c1.get_age())   # Accessing private attribute via public method
c1.set_age(4)         # Modifying private attribute via public method
print(c1.get_age())   # Verifying the change
