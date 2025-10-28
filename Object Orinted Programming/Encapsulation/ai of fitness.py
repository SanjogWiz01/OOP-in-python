class Fitness:
    def __init__(self, name, weight, calories_eaten):
        self.name = name
        self.weight = weight
        self.calories_eaten = calories_eaten
        self.__calorie_limit = 2000  # Private attribute

    # Method to add calories safely
    def doing_calories(self, calories):
        self.calories_eaten += calories
        if self.calories_eaten > self.__calorie_limit:
            print("⚠️ You’ve exceeded your calorie limit!")

    # Method to update weight
    def update_weight(self, weight):
        self.weight = weight

    # Display method
    def display_progress(self):
        print(f"Name: {self.name}")
        print(f"Weight: {self.weight} kg")
        print(f"Calories Eaten: {self.calories_eaten} kcal")
        print(f"Calorie Limit: {self.__calorie_limit} kcal")


# Create object
user1 = Fitness("Sanjog", 56, 1800)
user1.display_progress()

user1.doing_calories(300)   # Adds calories safely
user1.update_weight(57)      # Updates weight
user1.display_progress()     # Shows updated info
