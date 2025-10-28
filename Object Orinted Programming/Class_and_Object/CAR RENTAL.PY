class Car:
    def __init__(self, model, brand, price_per_day):
        self.model = model
        self.brand = brand
        self.price_per_day = price_per_day
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print(f"{self.brand} {self.model} has been rented.")
        else:
            print(f"{self.brand} {self.model} is not available.")

    def return_car(self):
        self.available = True
        print(f"{self.brand} {self.model} has been returned.")

    def __str__(self):
        status = "Available" if self.available else "Rented"
        return f"{self.brand} {self.model} - Rs.{self.price_per_day}/day - {status}"


class RentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_available_cars(self):
        print("\nAvailable Cars:")
        for car in self.cars:
            if car.available:
                print(car)

# --------- Test the system ------------
car1 = Car("Model S", "Tesla", 5000)
car2 = Car("Civic", "Honda", 2500)
car3 = Car("i10", "Hyundai", 1500)

system = RentalSystem()
system.add_car(car1)
system.add_car(car2)
system.add_car(car3)

system.show_available_cars()

car1.rent()
car1.rent()  # trying again

car1.return_car()
system.show_available_cars()
car2.rent()
system.show_available_cars()
