# Alex Voice
# import pyttsx3
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    print(f'Alex: {text}')
    engine.say(text)
    engine.runAndWait()
