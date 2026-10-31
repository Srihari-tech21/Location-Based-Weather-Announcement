import pyttsx3


def speak(text):
    """Convert the weather announcement into speech."""

    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 165)
        engine.setProperty("volume", 1.0)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception as error:
        print(f"Voice announcement failed: {error}")