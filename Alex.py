# Project Alex - Clarence Sarmiento
# Inspired by JARVIS in Iron Man
# Own version of Artificial Intelligence
# Import python package
from service import Alex_voice
from commands import users_voice
from service import task
from config import users_location


while True:
    print('Listening...')
    voice = users_voice.get()
    if 'hello' in voice:
        Alex_voice.speak('Hi there.')
    elif 'weather update' in voice:
        task.weather_update(users_location)
    elif 'time update' in voice:
        task.time()
    elif 'date' in voice:
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
    elif 'play' in voice:
        try:
            music = voice.split('play')[-1].strip().title().replace(' ', '_')
        except FileNotFoundError:
            music = voice.split('play')[-1].strip().title().replace(' ', '-')
        task.play_music(music)
    elif 'rest' in voice:
        Alex_voice.speak('Okay, Have a nice day.')
        exit()
    else:
        Alex_voice.speak('Command not registered.')
