from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
TTS_KEY = os.getenv("GOOGLE_TTS_KEY")
CALENDAR_KEY = os.getenv("CALENDAR_API_KEY")
TRANSLATE_KEY = os.getenv("GOOGLE_TRANSLATE_KEY")
WHISPER_KEY = os.getenv("WHISPER_API_KEY")
