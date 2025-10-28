class car:
    def __init__(self, make, model):
        self.name = make
        self.model = model

    def display_info(self):
        print("Car name:",self.name, "\nModel:", self.model)
    def __str__(self):
     return f"{self.name} is {self.model} years old."
my_car = car("Toyota", "Corolla")
my_car.display_info()