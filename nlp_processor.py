import re
import nltk
from nltk.tokenize import word_tokenize


# Download required NLTK tokenizer resources if missing.
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", quiet=True)

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)


def extract_city(text):
    """Extract a city name from a weather-related query."""

    text = text.strip()

    patterns = [
        r"\b(?:in|at|for|of)\s+([a-zA-Z][a-zA-Z\s.-]*?)(?:\?|!|\.|$)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            city = match.group(1).strip()

            city = re.sub(
                r"\b(today|tomorrow|now|currently|please|right now)\b.*$",
                "",
                city,
                flags=re.IGNORECASE
            ).strip()

            if city:
                return city

    return ""


def detect_intent(text):
    """Identify the weather information requested by the user."""

    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    # Sunrise and sunset must be checked before general weather.
    if any(word in text for word in ["sunrise", "sun rise", "dawn"]):
        return "sunrise"

    if any(word in text for word in ["sunset", "sun set", "dusk"]):
        return "sunset"

    # Feels-like temperature.
    if any(phrase in text for phrase in [
        "feels like",
        "feel like",
        "real feel",
        "apparent temperature",
        "feels hotter",
        "feels colder"
    ]):
        return "feels_like"

    # Atmospheric pressure.
    if any(word in text for word in [
        "pressure",
        "barometric"
    ]):
        return "pressure"

    # Visibility.
    if any(word in text for word in [
        "visibility",
        "visible",
        "how far can i see"
    ]):
        return "visibility"

    # Cloud coverage.
    if any(word in text for word in [
        "cloud",
        "cloudy",
        "clouds",
        "overcast"
    ]):
        return "clouds"

    # Humidity.
    if any(word in text for word in [
        "humidity",
        "humid",
        "moisture in the air"
    ]):
        return "humidity"

    # Wind.
    if any(word in text for word in [
        "wind",
        "windy",
        "breeze",
        "gust"
    ]):
        return "wind"

    # Rain-related questions.
    if any(word in text for word in [
        "rain",
        "raining",
        "rainfall",
        "precipitation",
        "drizzle"
    ]):
        return "rain"

    # Temperature.
    if any(word in text for word in [
        "temperature",
        "hot",
        "cold",
        "heat",
        "degrees"
    ]):
        return "temperature"

    # General weather conditions.
    return "weather"


def process_query(text):
    """Tokenize the query and return its city and intent."""

    tokens = word_tokenize(text)

    city = extract_city(text)
    intent = detect_intent(text)

    return {
        "tokens": tokens,
        "city": city,
        "intent": intent
    }