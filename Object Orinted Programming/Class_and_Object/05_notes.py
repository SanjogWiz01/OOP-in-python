class Student:
    def __init__(self, ok, oll):
        self.nae = ok    # instance variable
        self.rol = oll      # instance variable

# creating objects
s1 = Student("Sanjog", 101)
s2 = Student("Anita", 102)

print(s1.nae, s1.rol)   # Sanjog 101
print(s2.nae, s2.rol)   # Anita 102
