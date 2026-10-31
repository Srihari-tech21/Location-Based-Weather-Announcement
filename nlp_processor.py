import re
import nltk
from nltk.tokenize import word_tokenize

# Download the tokenizer data required by NLTK.
# This runs only when the required resource is missing.
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", quiet=True)

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)


def extract_city(text):
    """Extract a city name from a natural-language weather query."""

    text = text.strip()

    # Handle common phrases such as:
    # "weather in Vijayawada"
    # "temperature at Hyderabad"
    patterns = [
        r"\b(?:in|at|for|of)\s+([a-zA-Z][a-zA-Z\s.-]*?)(?:\?|!|\.|$)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            city = match.group(1).strip()

            # Remove common trailing phrases.
            city = re.sub(
                r"\b(today|now|currently|tomorrow|please|right now)\b.*$",
                "",
                city,
                flags=re.IGNORECASE,
            ).strip()

            if city:
                return city

    # Support a query containing only a city name.
    return text


def detect_intent(text):
    """Identify what weather information the user wants."""

    text = text.lower()

    if any(word in text for word in ["rain", "raining", "rainfall", "precipitation"]):
        return "rain"

    if any(word in text for word in ["humidity", "humid"]):
        return "humidity"

    if any(word in text for word in ["temperature", "hot", "cold", "heat"]):
        return "temperature"

    if any(word in text for word in ["wind", "windy", "breeze"]):
        return "wind"

    return "weather"


def process_query(text):
    """Tokenize the query and return its city and intent."""

    tokens = word_tokenize(text)
    city = extract_city(text)
    intent = detect_intent(text)

    return {
        "tokens": tokens,
        "city": city,
        "intent": intent,
    }