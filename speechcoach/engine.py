import pyttsx3
from gtts import gTTS
from phonemizer import phonemize
import os

class PronunciationEngine:
    def __init__(self):
        self.tts_engine = pyttsx3.init()

    def speak(self, text, lang):
        if lang == 'en':
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        else:
            tts = gTTS(text=text, lang=lang)
            tts.save("output.mp3")
            os.system("start output.mp3" if os.name == 'nt' else "afplay output.mp3")

    def phonetic(self, text, lang):
        if lang == 'en':
            return phonemize(text, language='en-us', backend='espeak', strip=True)
        else:
            return "Phonetic spelling only supported for English."
