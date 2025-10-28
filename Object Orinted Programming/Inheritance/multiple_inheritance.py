class Father:
    def skills(self):
        print("Coding")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()  # Father’s method is called (MRO)
c = Child()
c.skills()  # Father’s method is called (MRO)
