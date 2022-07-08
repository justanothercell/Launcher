import os.path
import shutil

import requests


def entry():
    print('Getting origin last commit sha...')
    sha = requests.get('https://api.github.com/repos/DragonFIghter603/Launcher/commits/main').json()['sha']

    try:
        with open('sha', 'r') as sha_file:
            read_sha = sha_file.read().strip()
    except FileNotFoundError:
        read_sha = 'null'

    print(f'Comparing commit shas {sha} and {read_sha}')

    if read_sha != sha:
        print('Updating...')

        if not os.path.exists('Launcher'):
            os.mkdir('Launcher')
        os.chdir('Launcher')
        print('Fetching git...')
        if os.name == 'nt':
            os.system('git fetch --all || (cd .. & rmdir launcher /s /q & git clone https://github.com/DragonFIghter603/Launcher.git & cd Launcher)')
            os.system('git reset --hard origin/main')
        else:
            os.system('git fetch --all || (cd .. ; rm launcher - r ; git clone https://github.com/DragonFIghter603/Launcher.git ; cd Launcher)')
            os.system('git reset --hard origin/main')
        print()
        print('Updating')
        shutil.copy('entrypoint.py', '../entrypoint.py')
        if os.path.isfile('../config.json'):
            shutil.copy('../config.json', 'config.json')
        else:
            shutil.copy('config.json', '../config.json')
        print('Building')
        __import__('Launcher.build_launcher').build_launcher.build()
        print()
        os.chdir('..')
        with open('sha', 'w') as sha_file:
            sha_file.write(sha)
        print('Updated sha in sha file')
        print('Finished updating')
        print()

    print('Continuing with main program...')
    print()


if __name__ == '__main__':
    entry()