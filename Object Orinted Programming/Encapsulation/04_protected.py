class Person:
    def __init__(self, name, age):
        self._name = name     # protected attribute
        self._age = age       # protected attribute

    def _display_info(self):   # protected method
        print(f"Name: {self._name}, Age: {self._age}")

class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

    def show_student(self):
        # accessing protected members inside subclass
        self._display_info()
        print(f"Roll No: {self.roll}")

# Object creation
s1 = Student("Sanjog", 18, 101)
s1.show_student()

# Technically possible (but not recommended)
print(s1._name)        # discouraged
s1._display_info()     # discouraged
