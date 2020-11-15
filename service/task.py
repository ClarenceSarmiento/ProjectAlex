# For performing tasks
import pyowm
import datetime
import webbrowser
import subprocess
import os
import wolframalpha
import wikipedia
import pywhatkit as kit
from pygame import mixer
from datetime import date
from config import owm_key
from config import client_key
from service import Alex_voice
from service import current
from commands import users_voice


def weather_update(location):
    owm = pyowm.OWM(owm_key)
    loc = owm.weather_manager().weather_at_place(location)
    weather = loc.weather
    temp = weather.temperature(unit='celsius')
    status = weather.detailed_status
    cleaned_temp_data = int(temp['temp'])
    Alex_voice.speak(f'The temperature today in {location} is {cleaned_temp_data} degree celsius.')
    Alex_voice.speak(f'The day today will have {status}.')


def time():
    now = datetime.datetime.now()
    time_12hour_format = now.strftime('%I:%M %p').lstrip("0")
    Alex_voice.speak(f"It's {time_12hour_format}")


def date_update():
    today = date.today()
    Alex_voice.speak(f'Today is {current.day_of_week(today.weekday())}.')
    Alex_voice.speak(f'{current.c_month(today.month)} {today.day}, {today.year}.')


def play_music(file_name):
    for root, dirs, files in os.walk(r'D:\Music'):
        for file in files:
            if file.endswith('.mp3'):
                names = (os.path.join(root, file))
                if file_name in names:
                    Alex_voice.speak(f'Now Playing {file_name}.')
                    mixer.init()
                    mixer.music.load(names)
                    mixer.music.play()


def search(voice):
    client = wolframalpha.Client(client_key)
    query = str(voice)
    try:
        try:
            res = client.query(query)
            result = next(res.results).text
            Alex_voice.speak(result)
        except BaseException:
            result = wikipedia.summary(query, sentences=2)
            Alex_voice.speak(result)
    except BaseException:
        url = "https://google.com/search?q=" + query
        webbrowser.get().open(url)


def website(voice):
    if 'youtube' in voice:
        Alex_voice.speak('What do you want to play?')
        youtube = users_voice.get()
        Alex_voice.speak(f'Playing {youtube}')
        kit.playonyt(youtube)
    elif 'google' in voice:
        Alex_voice.speak("What do you want to search for?")
        google = users_voice.get()
        Alex_voice.speak("Searching...")
        url = "https://google.com/search?q=" + google
        Alex_voice.speak(f'Here are the results for {google}.')
        webbrowser.get().open(url)
    elif 'facebook' in voice:
        Alex_voice.speak("Opening Facebook")
        url = "https://www.facebook.com/"
        webbrowser.get().open(url)
    elif 'location' in voice:
        Alex_voice.speak("What is the location?")
        location = users_voice.get()
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        Alex_voice.speak(f'Here is the location of {location}.')
        webbrowser.get().open(url)
    else:
        Alex_voice.speak(f"{voice} is not a website.")


def application(voice):
    if 'word' in voice:
        Alex_voice.speak("Running Microsoft Word")
        subprocess.Popen([r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'])
    elif 'powerpoint' in voice:
        Alex_voice.speak("Running Microsoft Powerpoint")
        subprocess.Popen([r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE'])
    elif 'excel' in voice:
        Alex_voice.speak("Running Microsoft Excel")
        subprocess.Popen([r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'])
    elif 'discord' in voice:
        Alex_voice.speak('Running Discord')
        subprocess.Popen(r'C:\Users\acer\AppData\Local\Discord\app-0.0.308\Discord.exe')
    else:
        Alex_voice.speak(f"{voice} is not an application.")
