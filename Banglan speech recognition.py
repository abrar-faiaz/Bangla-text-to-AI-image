import speech_recognition as sr
from translate import Translator

translator = Translator(from_lang="bn", to_lang="en")

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Tell me about the image you want to generate:")
    recognizer.adjust_for_ambient_noise(source)  # reduce background noise
    audio = recognizer.record(source, duration=5)  # record for 5 seconds

try:
    bangla_text = recognizer.recognize_sphinx(audio, language="bn-BD")
    print("You said:", bangla_text)
    english_text = translator.translate(bangla_text)
    print(english_text)
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")

