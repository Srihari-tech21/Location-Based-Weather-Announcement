import pyttsx3


_engine = None


def get_engine():
    """Initialize and reuse the speech engine."""

    global _engine

    if _engine is None:
        _engine = pyttsx3.init()

        # Speech speed: lower is slower, higher is faster.
        _engine.setProperty("rate", 155)

        # Volume ranges from 0.0 to 1.0.
        _engine.setProperty("volume", 1.0)

        # Prefer an installed English voice when available.
        voices = _engine.getProperty("voices")

        for voice in voices:
            voice_info = (
                f"{getattr(voice, 'id', '')} "
                f"{getattr(voice, 'name', '')}"
            ).lower()

            if "english" in voice_info or "en-" in voice_info:
                _engine.setProperty("voice", voice.id)
                break

    return _engine


def speak(text):
    """Speak an announcement using the configured voice."""

    if not text or not text.strip():
        print("No announcement text was provided.")
        return

    engine = None

    try:
        engine = get_engine()

        print("\nSpeaking announcement...")
        engine.say(text)
        engine.runAndWait()

    except Exception as error:
        print(f"Voice announcement failed: {error}")

    finally:
        if engine is not None:
            try:
                engine.stop()
            except Exception:
                pass