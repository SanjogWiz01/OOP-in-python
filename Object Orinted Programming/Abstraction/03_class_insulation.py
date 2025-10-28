from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

animal = Animal() # This will raise an error
# because we cannot instantiate an abstract class directly.
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
dog = Dog()
print(dog.make_sound())
