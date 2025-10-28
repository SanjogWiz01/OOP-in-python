class Cook:
    def __init__(self, recipe):
        self.recipe = recipe           # Public attribute
        self.__secret_ingredient = "Love"  # Private attribute

    def display_recipe(self):
        print(f"Recipe: {self.recipe}")
        print(f"Secret Ingredient: {self.__secret_ingredient}")

# Create an object
item = Cook("Pasta")
item.display_recipe()
