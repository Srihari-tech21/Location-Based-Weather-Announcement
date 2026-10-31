# Location-Based Weather Announcement System

## Overview

The Location-Based Weather Announcement System is a Python-based application that uses Natural Language Processing (NLP) to understand users' weather-related questions, retrieve live weather information for a specified city, and announce the results through speech.

The project combines NLP techniques, a weather API, and text-to-speech technology to provide an interactive weather information experience.

## Objectives

* Understand weather-related queries written in natural language.
* Extract city names from user queries.
* Identify intents such as temperature, humidity, rain, wind, and general weather.
* Retrieve current weather information using the OpenWeather API.
* Generate readable weather responses.
* Announce weather information using text-to-speech.

## Technologies Used

* **Programming Language:** Python
* **Natural Language Processing:** NLTK and regular expressions
* **Weather API:** OpenWeather API
* **HTTP Requests:** Requests library
* **Text-to-Speech:** pyttsx3
* **Environment Configuration:** python-dotenv
* **Development Environment:** Visual Studio Code

## Features

1. Natural-language weather queries.
2. Automatic city extraction.
3. Rule-based intent detection.
4. Live weather information retrieval.
5. Temperature and feels-like temperature reporting.
6. Humidity and wind-speed reporting.
7. Weather-condition reporting.
8. Optional voice announcements.
9. Error handling for invalid cities, API issues, and network failures.

## Project Structure

```text
Location-Based-Weather-Announcement/
├── main.py
├── nlp_processor.py
├── weather_service.py
├── voice_announcement.py
├── test_nlp.py
├── test_weather.py
├── test_voice.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

The `.env` file and `.venv` directory are created locally and should not be uploaded to GitHub.

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Location-Based-Weather-Announcement
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```text
OPENWEATHER_API_KEY=your_actual_openweather_api_key
```

Replace the placeholder with your own API key.

### 5. Run the application

```bash
python main.py
```

## Example Queries

* What is the weather in Vijayawada?
* What is the temperature in Hyderabad?
* What is the humidity in Chennai?
* Tell me the wind speed in Mumbai.
* Will it rain in Bengaluru?

## How It Works

1. The user enters a weather-related question.
2. The NLP processor tokenizes the input and detects the requested weather information.
3. The application extracts the city name.
4. The weather service sends a request to the OpenWeather API.
5. The API returns current weather information.
6. The application generates a response based on the detected intent.
7. The response is displayed as text and can optionally be spoken aloud.

## NLP Techniques

### Tokenization

NLTK tokenization divides the input sentence into individual tokens.

### City Extraction

Regular expressions identify the location mentioned in the query.

### Intent Detection

Rule-based keyword matching identifies whether the user is asking about temperature, rain, humidity, wind, or general weather.

## Limitations

* The current implementation uses rule-based NLP rather than a trained machine-learning language model.
* City extraction may not handle every complex sentence correctly.
* Weather information depends on API availability and the data returned by OpenWeather.
* Rain-related responses describe current reported conditions and do not provide a reliable forecast of future rainfall.
* Speech output depends on the local computer's audio configuration.

## Future Enhancements

* Speech recognition for voice-based input.
* Improved location extraction using named-entity recognition.
* Weather forecasts for upcoming hours and days.
* Automatic location detection with user permission.
* Multilingual announcements.
* A graphical user interface or web application.

## Conclusion

The Location-Based Weather Announcement System demonstrates how NLP techniques can be combined with external APIs and text-to-speech technology to create a practical application. It provides experience with natural-language query processing, API integration, response generation, and speech synthesis.
