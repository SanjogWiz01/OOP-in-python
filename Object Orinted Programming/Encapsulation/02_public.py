# 01_intro_encapsulation.py

class Student:
    def __init__(self, name, marks):
        self.name = name # public attribute 
        self.marks = marks  # Data inside class

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Object creation
s1 = Student("Sanjog", 85)
s1.display()
