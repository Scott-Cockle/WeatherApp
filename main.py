from weather_info import weather_data

weather_data = {city.lower(): data for city, data in weather_data.items()}

name_confirm = input("Hello! What is your name?: ")
print(f"\nWelcome {name_confirm}!")

location = input("\nWhich city would you like to know the weather for?: ")

location = location.lower()

def get_weather(city):
    if city in weather_data:
        data = weather_data[city]
        return (f"\nThe weather in {city} is currently: \n"
                f"Temperature: {data['temperature']}C\n"
                f"Conditions: {data['conditions']} \n"
                f"Wind MPH: {data['wind']} \n"
                f"Humidity: {data['humidity']} \n"
                f"\nThank you for using our weather app! We hope to see you again soon :)")
    else:
        return (f"\nSorry, I'm unable to gather information about the weather in {city} at this time.")

weather_info = get_weather(location)
print(weather_info)
