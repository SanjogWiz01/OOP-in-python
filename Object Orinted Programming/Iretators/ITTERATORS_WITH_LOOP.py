class RainyDayIterator:
    """
    Iterates only over rainy days
    """
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            if value.lower() == "rainy":
                return value
        raise StopIteration


# Example usage
if __name__ == "__main__":
    weather_data = ["Sunny", "Rainy", "Cloudy", "Rainy", "Windy"]
    for rainy_day in RainyDayIterator(weather_data):
        print(f"Take umbrella: {rainy_day}")