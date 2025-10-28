class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed  
    def __str__(self):
        return f"{self.name} is a {self.breed}"
my_dog = dog("Buddy", "Golden Retriever")
print(my_dog)  # Output: Buddy is a Golden Retrieverimal: --- IGNORE ---
# Output: Buddy says hello!