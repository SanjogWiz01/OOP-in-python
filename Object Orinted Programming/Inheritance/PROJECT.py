class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
    def display(self):
        print(f"Teacher: {self.name}, {self.age} yrs, {self.subject}, ${self.salary}")

class Student(Person):
    def __init__(self, name, age, grade, marks):
        super().__init__(name, age)
        self.grade = grade
        self.marks = marks
    def display(self):
        print(f"Student: {self.name}, {self.age} yrs, Grade: {self.grade}, Marks: {self.marks}")

t = Teacher("Mr. Sharma", 40, "Math", 500)
s = Student("Anita", 16, 10, 95)
t.display()
s.display()
