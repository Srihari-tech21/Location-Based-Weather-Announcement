from voice_announcement import speak
from nlp_processor import process_query
from weather_service import get_weather


def generate_response(result, intent):
    """Generate a natural-language weather response."""

    city = result["city"]
    country = result["country"]
    location = f"{city}, {country}"

    temperature = result["temperature"]
    feels_like = result["feels_like"]
    humidity = result["humidity"]
    description = result["description"]
    wind_speed = result["wind_speed"]

    if intent == "temperature":
        return (
            f"The current temperature in {location} is "
            f"{temperature} degrees Celsius."
        )

    elif intent == "feels_like":
        return (
            f"In {location}, the actual temperature is "
            f"{temperature} degrees Celsius, but it feels like "
            f"{feels_like} degrees Celsius."
        )

    elif intent == "humidity":
        return (
            f"The current humidity in {location} is "
            f"{humidity} percent."
        )

    elif intent == "wind":
        direction = result.get("wind_direction")

        if direction is None:
            return (
                f"The wind speed in {location} is "
                f"{wind_speed} meters per second."
            )

        return (
            f"The wind speed in {location} is "
            f"{wind_speed} meters per second, with a direction "
            f"of {direction} degrees."
        )

    elif intent == "rain":
        if "rain" in description.lower() or "drizzle" in description.lower():
            return (
                f"The current weather report for {location} "
                f"shows {description}. Rain-related conditions "
                f"are being reported."
            )

        return (
            f"The current reported conditions in {location} are "
            f"{description}. This current observation does not "
            f"tell us whether it will rain later."
        )

    elif intent == "pressure":
        pressure = result.get("pressure")

        if pressure is None:
            return f"Atmospheric pressure is unavailable for {location}."

        return (
            f"The atmospheric pressure in {location} is "
            f"{pressure} hectopascals."
        )

    elif intent == "visibility":
        visibility = result.get("visibility")

        if visibility is None:
            return f"Visibility information is unavailable for {location}."

        visibility_km = visibility / 1000

        return (
            f"The reported visibility in {location} is "
            f"{visibility_km:.1f} kilometers."
        )

    elif intent == "clouds":
        clouds = result.get("clouds")

        if clouds is None:
            return f"Cloud coverage is unavailable for {location}."

        return (
            f"Cloud coverage in {location} is "
            f"{clouds} percent. The reported weather condition "
            f"is {description}."
        )

    elif intent == "sunrise":
        return (
            f"Sunrise in {location} is at "
            f"{result['sunrise']} local time."
        )

    elif intent == "sunset":
        return (
            f"Sunset in {location} is at "
            f"{result['sunset']} local time."
        )

    return (
        f"The current weather in {location} is {description}. "
        f"The temperature is {temperature} degrees Celsius. "
        f"It feels like {feels_like} degrees Celsius. "
        f"Humidity is {humidity} percent, and wind speed is "
        f"{wind_speed} meters per second."
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

