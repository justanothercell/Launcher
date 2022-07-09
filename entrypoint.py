import os.path
import shutil

import requests

from Launcher.hashpath import path_checksum


def entry():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

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
        if not os.path.isfile('../flask_app.py'):
            shutil.copy('flask_app.py', '../flask_app.py')
        if os.path.isfile('../config.json'):
            shutil.copy('../config.json', 'config.json')
        else:
            shutil.copy('config.json', '../config.json')
        print()
        os.chdir('..')
        print('Updated sha in sha file')
        print('Finished updating')
        with open('sha', 'w') as sha_file:
            sha_file.write(sha)
        print()
        print('### Rerunning the new entrypoint just in case ###')
        __import__('Launcher.entrypoint').entrypoint.entry()
        print('### Finished rerunning the new entrypoint ###')
        print()
    print('Checking if need to rebuild...')
    try:
        with open('checksum', 'r') as checksum_file:
            read_checksum = checksum_file.read().strip()
    except FileNotFoundError:
        read_checksum = 'null'
    checksum = path_checksum(['Launcher/src', 'Launcher/pom.xml', 'config.json'])
    print(f'Comparing directory checksums of relevant files: {checksum} and {read_checksum}')
    if read_checksum != checksum:
        print('Building...')
        exe_name = __import__('Launcher.build_launcher').build_launcher.build()
        print('Copying executable to static')
        if not os.path.exists('static'):
            os.mkdir('static')
        shutil.copy(f'Launcher/target/{exe_name}', f'static/{exe_name}')
        with open('checksum', 'w') as checksum_file:
            checksum_file.write(checksum)
        print()
    print('Continuing with main program...')
    print()


if __name__ == '__main__':
    entry()