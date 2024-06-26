class WeatherStation():
    def __init__(self, location, temperature, humidity):
        self.locationn = location
        self.temperature = temperature
        self.humidity = humidity

    def display_weather(self):
        print(f"Weather at {self.location}:")
        print(f"Temperature: {self.temperature:.2f}°C and humidity: {self.humidity:.2f}%")

    def convert_to_fahrenheit(self):
        self.temperature = self.temperature * 9/5 + 32

    def convert_to_celsius(self):
        self.temperature = (self.temperature - 32) * 5/9

    def update_weather(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity