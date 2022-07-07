from flask import Flask, send_file, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return '<p>Hello, World!</p>'


@app.route('/download')
def download():
    if request.args.get('file') == 'launcher':
        return send_file('../../target/GladiatronLauncher.exe')
    if request.args.get('file') == 'application':
        return send_file('Application.zip')

@app.route('/verify')
def verify():
    return json.dumps({'success': True}), 200


@app.route('/get_version')
def get_version():
    return json.dumps({'success': True, 'version': "1.0.0"}), 200

app.run()
