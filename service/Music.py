import os
import random
from pygame import mixer
from service import Alex_voice

music_list = []


def play_music(voice):
    for root, dirs, files in os.walk(r'D:\Music'):
        for file in files:
            if file.endswith('.mp3'):
                names = (os.path.join(root, file))
                music_list.append(names)
                if 'list' in voice:
                    file_name = names.split('D:\\Music\\')[-1].strip()
                    print(file_name)
                elif 'play' in voice:
                    try:
                        music = voice.split('play')[-1].strip().title().replace(' ', '_')
                    except FileNotFoundError:
                        music = voice.split('play')[-1].strip().title().replace(' ', '-')
                    if music in names:
                        name = music.split('play')[-1].strip().title().replace('_', ' ')
                        Alex_voice.speak(f'Now Playing {name}.')
                        mixer.init()
                        mixer.music.load(names)
                        return mixer.music.play()
                elif 'random' in voice:
                    number = random.randint(0, len(music_list))
                    name = (os.path.join(root, files[number]))
                    mixer.init()
                    mixer.music.load(name)
                    return mixer.music.play()
                elif 'pause' in voice and 'unpause' not in voice:
                    Alex_voice.speak('Pausing Music')
                    return mixer.music.pause()
                elif 'unpause' in voice:
                    Alex_voice.speak('UnPausing Music')
                    return mixer.music.unpause()
                elif 'stop' in voice:
                    Alex_voice.speak('Stopping Music')
                    return mixer.music.stop()
                else:
                    return Alex_voice.speak('No music Available.')
