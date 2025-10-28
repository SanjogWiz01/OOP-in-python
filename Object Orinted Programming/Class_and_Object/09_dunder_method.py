class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):  #dunder method call automatically called in the class no need to call agai again in the object.
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
jhony = Dog("Jhony", 3)
print(jhony.name)  # Output: Jhony
print(jhony.age)   # Output: 3
print(Dog.species)  # Output: Canine
