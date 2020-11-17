# Project Alex - Clarence Sarmiento
# Inspired by JARVIS in Iron Man
# Own version of Artificial Intelligence
# Import python packages
from service import Alex_voice
from commands import users_voice
from service import task
from config import users_location


def alex():
    while True:
        Alex_voice.speak('I am now listening...')
        voice = users_voice.get()
        if 'hello' in voice:
            Alex_voice.speak('Hi there, what can I do for you?')
        elif 'weather' in voice:
            task.weather_update(users_location)
        elif 'time update' in voice:
            task.time_update()
        elif 'date' in voice and 'time and date' not in voice:
            task.date_update()
        elif 'time and date' in voice:
            task.time_update()
            task.date_update()
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
        elif 'note' in voice:
            note_text = users_voice.get()
            task.take_note(note_text)
        elif 'play' in voice:
            try:
                music = voice.split('play')[-1].strip().title().replace(' ', '_')
            except FileNotFoundError:
                music = voice.split('play')[-1].strip().title().replace(' ', '-')
            task.play_music(music)
        elif 'close' in voice:
            app = voice.split('close')[-1].strip()
            task.close(app)
        elif 'rest' in voice:
            Alex_voice.speak('Okay, Have a nice day.')
            exit()
        else:
            Alex_voice.speak('Command not registered.')

