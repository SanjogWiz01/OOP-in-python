from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):
    def fuel_type(self):
        print("Petrol")

class ElectricCar(Vehicle):
    def fuel_type(self):
        print("Electricity")

c = Car()
e = ElectricCar()
c.fuel_type()
e.fuel_type()
