from weather_service import get_weather


city = input("Enter a city name: ").strip()

if not city:
    print("Please enter a city name.")
else:
    result = get_weather(city)

    if "error" in result:
        print("\nError:", result["error"])
    else:
        print("\n========== LIVE WEATHER ==========")
        print(f"Location: {result['city']}, {result['country']}")
        print(f"Temperature: {result['temperature']} °C")
        print(f"Feels Like: {result['feels_like']} °C")
        print(f"Humidity: {result['humidity']}%")
        print(f"Conditions: {result['description']}")
        print(f"Wind Speed: {result['wind_speed']} m/s")
        print("==================================")