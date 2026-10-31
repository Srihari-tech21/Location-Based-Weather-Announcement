import os
import requests

from datetime import datetime, timezone
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch current weather information for a city."""

    if not API_KEY:
        return {
            "error": "API key is missing. Check your .env file."
        }

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=15
        )

        if response.status_code == 401:
            return {
                "error": "Invalid API key or the key is not active yet."
            }

        if response.status_code == 404:
            return {
                "error": f"City '{city}' was not found."
            }

        response.raise_for_status()

        data = response.json()

        main_data = data["main"]
        weather_data = data["weather"][0]
        wind_data = data.get("wind", {})
        sys_data = data.get("sys", {})

        # Convert sunrise and sunset timestamps to local city time.
        timezone_offset = data.get("timezone", 0)

        def format_local_time(timestamp):
            if not timestamp:
                return "Unavailable"

            local_timestamp = timestamp + timezone_offset

            return datetime.fromtimestamp(
                local_timestamp,
                tz=timezone.utc
            ).strftime("%I:%M %p")

        return {
            "city": data.get("name", city),
            "country": sys_data.get("country", "Unknown"),

            "temperature": round(main_data["temp"], 1),
            "feels_like": round(main_data["feels_like"], 1),

            "humidity": main_data["humidity"],
            "pressure": main_data.get("pressure", "Unavailable"),

            "description": weather_data.get(
                "description",
                "Unknown conditions"
            ),

            "wind_speed": wind_data.get("speed", 0),
            "wind_direction": wind_data.get("deg"),

            "visibility": data.get("visibility"),
            "clouds": data.get("clouds", {}).get("all"),

            "sunrise": format_local_time(
                sys_data.get("sunrise")
            ),

            "sunset": format_local_time(
                sys_data.get("sunset")
            )
        }

    except requests.exceptions.Timeout:
        return {
            "error": "The weather service timed out."
        }

    except requests.exceptions.ConnectionError:
        return {
            "error": "Unable to connect. Check your internet connection."
        }

    except requests.exceptions.HTTPError:
        return {
            "error": "The weather API request failed."
        }

    except (KeyError, ValueError, TypeError):
        return {
            "error": "The weather service returned unexpected data."
        }