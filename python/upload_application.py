import json
import os
import shutil

import discord
import requests
from discord import Webhook, AsyncWebhookAdapter
import aiohttp as aiohttp
import asyncio

webhook_url = 'https://discord.com/api/webhooks/895386870811353199/c7FzBLMl__5DzCmnUB1rwTDVOp2MSq-GsLKtU5Z9gVWlEPB8Or3VIR0emOwm0OtFT5fL'

base_url = 'https://dragonfighter603.eu.pythonanywhere.com'

def do_build(manual: bool):
    files = []
    for file in os.listdir('Application'):
        files.append(file)

    assert len(files) == 1, f'Expected 1 file, got {len(files)}'
    print(f'Building version "{files[0]}"')

    if manual:
        if input(f'Building version "{files[0]}". confirm? y/n:').lower() != 'y':
            exit()

    print('Zipping...')
    shutil.make_archive('Application', 'zip', 'Application')
    print('Finished!')

    if manual:
        if input(f'Upload version "{files[0]}" to server? y/n:').lower() != 'y':
            exit()
    print('uploading...')
    with open('Application.zip', 'rb') as application:
        response = requests.post(base_url+'/upload?'
                                                  'id=yAxvoR9z8v3AlXqTejkNEQO94NXLPufA&'
                                                  'password=vz5Ou4MPobjeKDW14GtWDqu8JrKGQGanE4NOiJqG5xkrU5IiZBJpvszZxJHc8LkI&'
                                                  'file=application&'
                                                  'version='+files[0], files={'zipfile': application})

    if response.ok:
        print('Upload completed successfully!')
        print(response.text)
        return files[0]
    else:
        print('Something went wrong!')
        print(response.text)
        return None


async def send_notification(build: str):
    if build is None:
        return
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
        e = discord.Embed(title='Build ' + build, description='Check out the new build!')
        e.add_field(name='Info', value="""glhf with inverted normals >[^^]<
        """, inline=False)
        await webhook.send('@everyone', embed=e)


loop = asyncio.get_event_loop()
# loop.run_until_complete(send_notification(do_build(False)))
# loop.run_until_complete(test_message())
# do_build(False)

loop.run_until_complete(send_notification(do_build(False)))
loop.close()
