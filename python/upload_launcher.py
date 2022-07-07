import requests

base_url = 'https://dragonfighter603.eu.pythonanywhere.com'

with open('../src/main/resources/version', 'r') as v:
    version = v.readlines()[0].strip()

with open("../target/GladiatronLauncher.exe", "rb") as launcher:
    response = requests.post(base_url + '/upload?'
                                        'id=yAxvoR9z8v3AlXqTejkNEQO94NXLPufA&'
                                        'password=vz5Ou4MPobjeKDW14GtWDqu8JrKGQGanE4NOiJqG5xkrU5IiZBJpvszZxJHc8LkI&'
                                        'file=launcher&'
                                        'version=' + version, files={'zipfile': launcher})

print(f'Uploaded launcher v:{version}')

print(f'{response.status_code}: {response.reason}')

print(response.json())
