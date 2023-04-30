from random import choice
import speech_recognition as sr
from config import config

recognizer = sr.Recognizer()
services = {
    'openai': recognizer.recognize_whisper_api,
    'whisper': recognizer.recognize_whisper,
    'google': recognizer.recognize_google,
}

def get_openai_key() -> str:
    return choice(config['OPENAPI_KEYS'])
