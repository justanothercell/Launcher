import os

requirements = [
    'certifi==2022.6.15',
    'charset-normalizer==2.1.0',
    'click==8.1.3',
    'colorama==0.4.5',
    'Flask==2.1.2',
    'idna==3.3',
    'itsdangerous==2.1.2',
    'Jinja2==3.1.2',
    'MarkupSafe==2.1.1',
    'requests==2.28.1',
    'urllib3==1.26.10',
    'Werkzeug==2.1.2'
]

with open('requirements.txt', 'w') as req:
    req.write('\n'.join(requirements))

print('Installing requirements...')
os.system(f'pip install -r requirements.txt')
print()

import urllib.request

if __name__ == '__main__':
    print('Starting...')
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    if not os.path.exists('res'):
        os.mkdir('res')
    print('Fetching assets...')

    urllib.request.urlretrieve('https://raw.githubusercontent.com/DragonFIghter603/Launcher/main/entrypoint.py', 'entrypoint.py')
    urllib.request.urlretrieve('https://raw.githubusercontent.com/DragonFIghter603/Launcher/main/res/icon.png', 'res/icon.png')
    urllib.request.urlretrieve('https://raw.githubusercontent.com/DragonFIghter603/Launcher/main/res/icon.ico', 'res/icon.ico')

    print('Starting entrypoint.py')
    print()
    __import__('entrypoint').entry()