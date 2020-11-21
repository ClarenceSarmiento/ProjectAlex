# For performing tasks
import pyowm
import datetime
import webbrowser
import subprocess
import os
import wolframalpha
import wikipedia
import pywhatkit as kit
from datetime import date
from config import owm_key
from config import client_key
from service import Alex_voice
from service import current
from commands import users_voice


def greet(name):
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        Alex_voice.speak(f'Good Morning {name}!')
    elif 12 <= current_hour < 18:
        Alex_voice.speak(f'Good Afternoon {name}!')
    elif current_hour >= 18 and current_hour != 0:
        Alex_voice.speak(f'Good Evening {name}!')
    else:
        pass


def time_update():
    now = datetime.datetime.now()
    time_12hour_format = now.strftime('%I:%M %p').lstrip("0")
    return Alex_voice.speak(f"It's {time_12hour_format}")


def date_update():
    today = date.today()
    return Alex_voice.speak(f'Today is {current.day_of_week(today.weekday())}, '
                            f'{current.c_month(today.month)} {today.day}, {today.year}.')


def weather_update(location):
    owm = pyowm.OWM(owm_key)
    loc = owm.weather_manager().weather_at_place(location)
    weather = loc.weather
    temp = weather.temperature(unit='celsius')
    status = weather.detailed_status
    cleaned_temp_data = int(temp['temp'])
    return Alex_voice.speak(f'The temperature today in {location} is {cleaned_temp_data} degree celsius. '
                            f'The day today will have {status}.')


def search(voice):
    client = wolframalpha.Client(client_key)
    query = str(voice)
    try:
        try:
            res = client.query(query)
            result = next(res.results).text
            return Alex_voice.speak(result)
        except BaseException:
            result = wikipedia.summary(query, sentences=2)
            return Alex_voice.speak(result)
    except BaseException:
        url = "https://google.com/search?q=" + query
        return webbrowser.get().open(url)


def take_note(voice):
    current_date = datetime.datetime.now()
    file_name = str(current_date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(voice)
    subprocess.Popen(["notepad.exe", file_name])
    return Alex_voice.speak("I made a note out of that.")


def website(voice):
    if 'youtube' in voice:
        Alex_voice.speak('What do you want to play?')
        print('>>|Speak|')
        youtube = users_voice.get()
        Alex_voice.speak(f'Playing {youtube}')
        return kit.playonyt(youtube)
    elif 'google' in voice:
        Alex_voice.speak("What do you want to search for?")
        print('>>|Speak|')
        google = users_voice.get()
        google = google.split('search for')[-1].strip()
        Alex_voice.speak("Searching...")
        url = "https://google.com/search?q=" + google
        Alex_voice.speak(f'Here are the results for {google}.')
        return webbrowser.get().open(url)
    elif 'facebook' in voice:
        Alex_voice.speak("Opening Facebook")
        url = "https://www.facebook.com/"
        return webbrowser.get().open(url)
    elif 'location' in voice:
        Alex_voice.speak("What is the location?")
        print('>>|Speak|')
        location = users_voice.get()
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        Alex_voice.speak(f'Here is the location of {location}.')
        return webbrowser.get().open(url)
    elif 'github' in voice:
        Alex_voice.speak('Opening Github')
        url = 'https://github.com/'
        return webbrowser.get().open(url)
    else:
        return Alex_voice.speak(f"{voice} is not available.")


def application(voice):
    if 'word' in voice or 'microsoft word' in voice:
        Alex_voice.speak("Running Microsoft Word")
        return subprocess.Popen([r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'])
    elif 'powerpoint' in voice or 'microsoft powerpoint' in voice:
        Alex_voice.speak("Running Microsoft Powerpoint")
        return subprocess.Popen([r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE'])
    elif 'excel' in voice or 'microsoft excel' in voice:
        Alex_voice.speak("Running Microsoft Excel")
        return subprocess.Popen([r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'])
    elif 'discord' in voice:
        Alex_voice.speak('Running Discord')
        return subprocess.Popen(r'C:\Users\acer\AppData\Local\Discord\app-0.0.308\Discord.exe')
    elif 'windows explorer' in voice:
        Alex_voice.speak('Running Windows Explorer')
        return subprocess.Popen(r'C:\Windows\explorer.exe')
    else:
        return Alex_voice.speak(f"{voice} is not available.")


def computer(voice):
    if 'documents' in voice:
        Alex_voice.speak('Accessing Computer Documents')
        return os.startfile(r'C:\Users\acer\Documents')
    elif 'downloads' in voice:
        Alex_voice.speak('Accessing Computer Downloads')
        return os.startfile(r'C:\Users\acer\Downloads')
    elif 'pictures' in voice:
        Alex_voice.speak('Accessing Computer Pictures')
        return os.startfile(r'C:\Users\acer\Pictures')
    elif 'music' in voice:
        Alex_voice.speak('Accessing Computer Music')
        return os.startfile(r'C:\Users\acer\Music')
    elif 'videos' in voice:
        Alex_voice.speak('Accessing Computer Videos')
        return os.startfile(r'C:\Users\acer\Videos')
    else:
        return Alex_voice.speak(f"{voice} is not available.")


def close(voice):
    if 'word' in voice or 'microsoft word' in voice:
        Alex_voice.speak('Closing Microsoft Word')
        return os.system('taskkill/f /im WINWORD.EXE')
    elif 'powerpoint' in voice or 'microsoft powerpoint' in voice:
        Alex_voice.speak('Closing Microsoft Powerpoint')
        return os.system('taskkill/f /im POWERPNT.EXE')
    elif 'excel' in voice or 'microsoft excel' in voice:
        Alex_voice.speak("Closing Microsoft Excel")
        return os.system('taskkill/f /im EXCEL.EXE')
    elif 'discord' in voice:
        Alex_voice.speak('Closing Discord')
        return os.system('taskkill/f /im Discord.exe')
    elif 'windows explorer' in voice:
        Alex_voice.speak('Closing Windows Explorer')
        return os.system('taskkill/f /im explorer.exe')
    elif 'browser' in voice:
        Alex_voice.speak('Closing Browser')
        return os.system('taskkill/f /im chrome.exe')
    elif 'notepad' in voice:
        Alex_voice.speak('Closing Notepad')
        return os.system('taskkill/f /im notepad.exe')
    else:
        return Alex_voice.speak(f"{voice} is not open.")
