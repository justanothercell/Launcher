import os

if __name__ == '__main__':
    os.mkdir('res')
    with open('https://raw.githubusercontent.com/DragonFIghter603/Launcher/main/entrypoint.py', 'r') as src:
        with open('entrypoint.py', 'w') as entrypoint:
            entrypoint.write(src.read())

    with open('https://raw.githubusercontent.com/DragonFIghter603/Launcher/main/res/icon.png', 'r') as src:
        with open('res/icon.png', 'w') as icon:
            icon.write(src.read())

    with open('https://raw.githubusercontent.com/DragonFIghter603/Launcher/main/res/icon.ico', 'r') as src:
        with open('res/icon.ico', 'w') as icon:
            icon.write(src.read())

    __import__('entrypoint').entry()