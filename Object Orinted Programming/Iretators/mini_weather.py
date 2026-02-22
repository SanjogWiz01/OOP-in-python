def weather_generator(data):
    """
    Generator function to yield weather data one by one
    """
    for item in data:
        yield item


# Example usage
if __name__ == "__main__":
    weather_data = ["Sunny", "Rainy", "Cloudy", "Windy"]
    for day in weather_generator(weather_data):
        print(f"Forecast: {day}")