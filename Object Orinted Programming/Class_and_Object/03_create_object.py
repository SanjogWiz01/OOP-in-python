class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
# Creating an object
sanjog=student("sanjog poudel",17)
print(f"Name: {sanjog.name} Age: {sanjog.age}")
# alternatively
print("Name:", sanjog.name,'Age:', sanjog.age)