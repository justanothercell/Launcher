import os
import shutil
import urllib.request

import requests

if __name__ == '__main__':
    print('Starting...')
    if not os.path.exists('res'):
        os.mkdir('res')
    print('Fetching assets...')

    urllib.request.urlretrieve('https://raw.githubusercontent.com/DragonFIghter603/Launcher/main/entrypoint.py', 'entrypoint.py')
    urllib.request.urlretrieve('https://raw.githubusercontent.com/DragonFIghter603/Launcher/main/res/icon.png', 'res/icon.png')
    urllib.request.urlretrieve('https://raw.githubusercontent.com/DragonFIghter603/Launcher/main/res/icon.ico', 'res/icon.ico')

    print('Starting entrypoint.py')
    print()
    __import__('entrypoint').entry()