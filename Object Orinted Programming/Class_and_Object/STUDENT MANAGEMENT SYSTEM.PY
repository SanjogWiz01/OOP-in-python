class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"{self.roll}. {self.name} - Marks: {self.marks}")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll, marks):
        student = Student(name, roll, marks)
        self.students.append(student)

    def show_all(self):
        print("\nStudent List:")
        for s in self.students:
            s.display()

# ---------- Test ----------
manager = StudentManager()
manager.add_student("Sanjog", 1, 92)
manager.add_student("Aayush", 2, 85)
manager.show_all()
manager.add_student("Rita", 3, 78)
manager.show_all()