class WeatherIterator:
    """
    Custom iterator for daily weather readings
    """
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


# Example usage
if __name__ == "__main__":
    weather_data = ["Sunny", "Rainy", "Cloudy", "Windy"]
    it = WeatherIterator(weather_data)

    for day in it:
        print(f"Weather today: {day}")