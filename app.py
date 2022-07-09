from flask import Flask, send_file, request, redirect
import json


app = Flask(__name__)


print('Loading config.json')
with open('config.json') as config_json:
    config = json.load(config_json)
try:
    launcher_config = config['launcher']
    app_config = config['app']
    launcher_name = launcher_config['name']
    app_download_url = app_config['download_url']
    app_version_url = app_config['download_url']
except KeyError as e:
    print('Error while loading config.json:')
    print(f'Expected key {e}')
    print('Aborting!')
    raise e
print()

with open('checksum', 'r') as checksum_file:
    launcher_version = checksum_file.read().strip()


@app.route('/download')
def download():
    if request.args.get('file') == 'launcher':
        return send_file(f'static/{launcher_name}.exe')
    if request.args.get('file') == 'application':
        return redirect(app_download_url)
    return json.dumps({'success': False, 'reason': 'bad request'}), 400


@app.route('/verify')
def verify():
    return json.dumps({'success': True}), 200


@app.route('/get_version')
def get_version():
    if request.args.get('file') not in ['application', 'launcher']:
        return json.dumps({'success': False, 'reason': 'bad request'}), 400
    if request.args.get('file') == 'launcher':
        return json.dumps({'success': True, 'version': launcher_version}), 200
    if request.args.get('file') == 'application':
        return redirect(app_version_url)


if __name__ == '__main__':
    app.run()
