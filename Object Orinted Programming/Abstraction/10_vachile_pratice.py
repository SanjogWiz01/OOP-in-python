from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Derived class
class Bike(Vehicle):

    def start(self):
        print("Bike Started")


# Main Program
b = Bike()
b.start()