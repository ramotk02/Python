from weather_station import WeatherStation
from datetime import datetime
import random


def create_weather_station():
    location = input("Enter the location: ")
    try:
        temperature = float(input("Enter the temperature in Celsius: "))
        humidity = float(input("Enter the humidity (percentage): "))
        return WeatherStation(location, temperature, humidity)
    except ValueError:
        print("Invalid input. Please enter numeric values for temperature and humidity.")
        return None
    
def update_weather_station(weather_station):
    try:
        temperature = float(input("Enter the new temperature in Celsius: "))
        humidity = float(input("Enter the new humidity (percentage): "))
        weather_station.update_weather(temperature, humidity)
    except ValueError:
        print("Invalid input. Please enter numeric values for temperature and humidity.")

def display_menu():
    print("\nWeather Station Menu:")
    print("1. Create a new weather station")
    print("2. Update the weather conditions")
    print("3. Convert the temperature to Fahrenheit")
    print("4. Convert the temperature to Celsius")
    print("5. Display current weather conditions")
    print("6. Exit")

def main():
    weather_station = None

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                weather_station = create_weather_station()
                if weather_station:
                    print("Weather station created successfully.")

            elif choice == 2:
                if weather_station:
                    update_weather_station(weather_station)
                else:
                    print("Please create a weather station first.")

            elif choice == 3:
                if weather_station:
                    fahrenheit = weather_station.convert_to_fahrenheit()
                    print(f"Temperature in Fahrenheit: {fahrenheit}°F")
                else:
                    print("Please create a weather station first.")

            elif choice == 4:
                if weather_station:
                    celsius = weather_station.convert_to_celsius()
                    print(f"Temperature in Celsius: {celsius}°C")
                else:
                    print("Please create a weather station first.")

            elif choice == 5:
                if weather_station:
                    print(f"\nCurrent date and time: {datetime.now()}")
                    weather_station.display_weather()
                else:
                    print("Please create a weather station first.")

            elif choice == 6:
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")

