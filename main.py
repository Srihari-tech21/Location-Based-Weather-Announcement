from voice_announcement import speak
from nlp_processor import process_query
from weather_service import get_weather


def generate_response(result, intent):
    """Generate a response based on the requested weather information."""

    city = result["city"]
    country = result["country"]
    temperature = result["temperature"]
    feels_like = result["feels_like"]
    humidity = result["humidity"]
    description = result["description"]
    wind_speed = result["wind_speed"]

    location = f"{city}, {country}"

    if intent == "temperature":
        return (
            f"The temperature in {location} is {temperature} degrees Celsius. "
            f"It feels like {feels_like} degrees Celsius."
        )

    elif intent == "rain":
        if "rain" in description.lower() or "drizzle" in description.lower():
            return f"Rain-related conditions are reported in {location}: {description}."
        else:
            return (
                f"The current reported conditions in {location} are {description}. "
                "This does not guarantee that it will not rain."
            )

    elif intent == "humidity":
        return f"The humidity in {location} is {humidity} percent."

    elif intent == "wind":
        return f"The wind speed in {location} is {wind_speed} meters per second."

    else:
        return (
            f"The current weather in {location} is {description}. "
            f"The temperature is {temperature} degrees Celsius, "
            f"humidity is {humidity} percent, "
            f"and wind speed is {wind_speed} meters per second."
        )


def main():
    print("\n==========================================")
    print("   LOCATION-BASED WEATHER ANNOUNCEMENT")
    print("==========================================")
    print("Ask about weather, temperature, rain, humidity, or wind.")
    print("Type 'exit' to close the application.")

    while True:
        query = input("\nEnter your weather question: ").strip()

        if query.lower() in {"exit", "quit", "bye"}:
            print("\nThank you for using the Weather Announcement System!")
            break

        if not query:
            print("Please enter a weather question.")
            continue

        processed = process_query(query)
        city = processed["city"]
        intent = processed["intent"]

        if not city:
            print("Please mention a city name.")
            continue

        print(f"\nDetected city: {city}")
        print(f"Detected intent: {intent}")
        print("Fetching live weather information...")

        weather = get_weather(city)

        if "error" in weather:
            print(f"\nError: {weather['error']}")
            continue

        response = generate_response(weather, intent)

        print("\n---------- WEATHER ANNOUNCEMENT ----------")
        print(response)
        print("------------------------------------------")

    
        choice = input("Would you like to hear the announcement? (yes/no): ").strip().lower()

        if choice in {"yes", "y"}:
            print("Speaking weather announcement...")
            speak(response)


if __name__ == "__main__":
    main()

