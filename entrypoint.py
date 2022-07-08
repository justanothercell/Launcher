import os.path
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

        with open('sha', 'w') as sha_file:
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
        print('Launching update script...')
        os.system('start python cp_entry.py')
        print('Exiting')
        exit(0)

    print('Continuing with main program...')
    print()


if __name__ == '__main__':
    entry()