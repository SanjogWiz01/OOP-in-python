
class Person: # given arguments  >>>>> with default values
    def __init__(self, name="Unknown", age=18): # Default values provided
        self.name = name
        self.age = age

p1 = Person("Sanjog", 19) # Using custom values
p2 = Person()
print(p1.name, p1.age)
print(p2.name, p2.age)
