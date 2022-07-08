import os
import shutil

import requests

if __name__ == '__main__':
    print('Starting...')
    os.mkdir('res')
    print('Fetching assets...')
    with open('entrypoint.py', 'w') as entrypoint:
        entrypoint.write(requests.get('https://raw.githubusercontent.com/DragonFIghter603/Launcher/main/entrypoint.py').text)

    with open('res/icon.png', 'wb') as icon:
        r = requests.get('https://raw.githubusercontent.com/DragonFIghter603/Launcher/main/res/icon.png')
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, icon)

    with open('res/icon.ico', 'wb') as icon:
        r = requests.get('https://raw.githubusercontent.com/DragonFIghter603/Launcher/main/res/icon.ico')
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, icon)

    print('Starting entrypoint.py')
    print()
    __import__('entrypoint').entry()