class Parent:
    def info(self):
        print("Parent info")

class Child1(Parent):
    def display(self):
        print("Child1 info")

class Child2(Parent):
    def display(self):
        print("Child2 info")

c1 = Child1()
c2 = Child2()
c1.info()
c2.info()
