class Grandparent:
    def message(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def welcome(self):
        print("Hello from Child")

c = Child()
c.message()
c.greet()
c.welcome()
c = Child()
c.message()
c.greet()
