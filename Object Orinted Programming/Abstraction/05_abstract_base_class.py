"""
Using abstract base class to enforce abstraction.
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")

# Demo
vehicles = [Car(), Bike()]
for v in vehicles:
    v.start_engine()