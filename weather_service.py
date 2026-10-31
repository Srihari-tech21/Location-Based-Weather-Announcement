import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    if not API_KEY:
        return {"error": "API key is missing. Check your .env file."}

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
            return {"error": f"City '{city}' was not found."}

        response.raise_for_status()

        data = response.json()

        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

    except requests.exceptions.Timeout:
        return {"error": "The weather service timed out."}

    except requests.exceptions.ConnectionError:
        return {
            "error": "Unable to connect. Check your internet connection."
        }

    except requests.exceptions.HTTPError as error:
        return {"error": f"Weather API request failed: {error}"}

    except (KeyError, ValueError, TypeError):
        return {"error": "The weather service returned unexpected data."}
