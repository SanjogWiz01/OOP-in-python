class Student:
    school = "PEC"

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"{self.name} ({self.roll}) - {self.marks}")

s1 = Student("Sanjog", 1, 90)
s2 = Student("Aayush", 2, 85)

s1.display()
s2.display()
print("School:", Student.school)
print("School:", s1.school)
print("School:", s2.school)
