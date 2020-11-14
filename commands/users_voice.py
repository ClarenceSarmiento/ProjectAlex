# Collecting users voice
# import speech recognition
import speech_recognition as sr
from service import Alex_voice


def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        voice_data = " "
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Alex_voice.speak('Sorry, I did not understand you.')
            print('Listening....!')
            return get()
        except sr.RequestError:
            Alex_voice.speak('Sorry, my speech service is down.')
        return voice_data.lower()
