# Project Alex - Clarence Sarmiento
# Inspired by JARVIS in Iron Man
# Own version of Artificial Intelligence
# Import python packages
from commands import users_voice
from service import task
from service import Schedule_finder
from service import Alex_voice
from service import Music
from config import users_location


def alex():
    task.date_update()
    Schedule_finder.schedule('today')
    task.weather_update(users_location)
    Alex_voice.speak('I am now listening...')
    while True:
        print('>>|Speak|')
        voice = input('>> ')# users_voice.get()
        if 'hello' in voice:
            Alex_voice.speak('Hi there, what can I do for you?')
        elif 'weather update' in voice:
            task.weather_update(users_location)
        elif 'time update' in voice:
            task.time_update()
        elif 'date today' in voice:
            task.date_update()
        elif 'time and date' in voice:
            task.time_update()
            task.date_update()
        elif 'what do i have on' in voice:
            sched = voice.split('what do i have on')[-1].strip()
            Schedule_finder.schedule(sched)
        elif 'open' in voice:
            site = voice.split('open')[-1].strip()
            task.website(site)
        elif 'run' in voice:
            app = voice.split('run')[-1].strip()
            task.application(app)
        elif 'computer' in voice:
            pc = voice.split('computer')[-1].strip()
            task.computer(pc)
        elif 'search' in voice:
            search = voice.split('search')[-1].strip()
            task.search(search)
        elif 'remember this' in voice:
            Alex_voice.speak('What is it?')
            print('>>|Speak|')
            note_text = users_voice.get()
            task.take_note(note_text)
        elif 'music' in voice:
            music = voice.split('music')[-1].strip()
            Music.play_music(music)
        elif 'close' in voice:
            app = voice.split('close')[-1].strip()
            task.close(app)
        elif 'rest' in voice:
            Alex_voice.speak('Okay, Have a nice day.')
            exit()
        else:
            Alex_voice.speak('Command not registered.')
        Alex_voice.speak('Anything else?')


alex()
