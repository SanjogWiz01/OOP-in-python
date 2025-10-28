class CoffeeMachine:
    def __init__(self):
        self.__water_level = 0

    def fill_water(self, amount):
        self.__water_level += amount
        print(f"Water filled: {amount}ml")

    def make_coffee(self):
        if self.__water_level >= 200:
            self.__boil_water()
            print("☕ Coffee is ready!")
            self.__water_level -= 200
        else:
            print("Not enough water!")

    def __boil_water(self):
        print("Boiling water...")

# Demo
machine = CoffeeMachine()
machine.fill_water(300)
machine.make_coffee()