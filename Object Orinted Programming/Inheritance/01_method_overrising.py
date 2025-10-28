class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

c = Child()
c.greet()  # Child’s method is called
c = Child()
c.greet()  # Child’s method is called
c = Child()
c.greet()  # Child’s method is called