import os.path


def entry():
    if not os.path.exists('Launcher'):
        os.mkdir('Launcher')

    os.chdir('Launcher')

    if os.name == 'nt':
        os.system('git fetch --all || (cd .. & rmdir launcher /s /q & git clone https://github.com/DragonFIghter603/Launcher.git & cd Launcher)')
        os.system('git reset --hard origin/main')
    else:
        os.system('git fetch --all || (cd .. ; rm launcher - r ; git clone https://github.com/DragonFIghter603/Launcher.git ; cd Launcher)')
        os.system('git reset --hard origin/main')

    os.system('start python launcher/cp_entry.py')


if __name__ == '__main__':
    entry()