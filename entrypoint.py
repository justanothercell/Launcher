import os.path
import requests


def entry():
    sha = requests.get('https://api.github.com/repos/DragonFIghter603/Launcher/commits/main').json()['sha']

    if not os.path.exists('sha1'):
        with open('sha', 'w') as sha_file:
            sha_file.write('0')

    with open('sha', 'w') as sha_file:
        if sha_file.read().strip() != sha:
            sha_file.write(sha)

            if not os.path.exists('Launcher'):
                os.mkdir('Launcher')
            os.chdir('Launcher')
            if os.name == 'nt':
                os.system('git fetch --all || (cd .. & rmdir launcher /s /q & git clone https://github.com/DragonFIghter603/Launcher.git & cd Launcher)')
                os.system('git reset --hard origin/main')
            else:
                os.system('git fetch --all || (cd .. ; rm launcher - r ; git clone https://github.com/DragonFIghter603/Launcher.git ; cd Launcher)')
                os.system('git reset --hard origin/main')

            os.system('start python cp_entry.py')
            exit(0)


if __name__ == '__main__':
    entry()