class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

def make_sound(animal):
    animal.speak()

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)
make_sound(d)