class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def welcome(self):
        print("Welcome from Child")

c = Child()
c.greet()
c.welcome()
c = Child()
c.greet()