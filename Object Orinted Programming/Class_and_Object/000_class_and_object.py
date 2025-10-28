class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} says hello!"
dog = animal("Buddy", "Dog")
print(dog.speak())