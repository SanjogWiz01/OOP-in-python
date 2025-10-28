''' 🏋️‍♂️ Project Topic: FitnessTracker – Calorie and Weight Management
🎯 Concept

You’ll make a class that:

Stores user details (name, weight, calories eaten).

Keeps the calorie limit private.

Allows updating calories and weight using methods.

Displays fitness progress through a public method.'''
class fitness:
    def __init__(self,name,weight,calories_eaten):
        self.name = name
        self.weight = weight
        self.calories_eaten = calories_eaten
        self.__calorie_limit = 2000  # Private attribute 
        '''
    def doing_calories(self,calories):
            self.calories_eaten += calories
            if self.calories_eaten > self.__calorie_limit:
              print(" You’ve exceeded your calorie limit!")
    def update_weight(self,weight):
            self.weight = weight '''
    def display_progress(self):
            print(f"Name: {self.name}")
            print(f"Weight: {self.weight} kg")
            print(f"Calories Eaten: {self.calories_eaten} kcal")
            print(f"Calorie Limit: {self.__calorie_limit} kcal")
# Create an object
user1 = fitness("sanjog", 56, 5000)
user1.display_progress()
 #er1.doing_calories(300)
'''
user1.update_weight(60)'''