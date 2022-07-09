# Launcher
 A launcher to auto update your application


### How to use
This is configured to work on [PythonAnywhere](https://www.pythonanywhere.com/):
it has `flask_app.py` in the server home folder, which provides the `app` variable.

If you use any other provider that requires a specific entry point file, create that provider specific entrypoint file
and get access to app by adding `from flask_app import app` at the top.

If anything breaks during updating, you can fix it 95% of the time by copying
`Launcher/entrypoint.py` to `entrypoint.py`.

1. copy `init.py` into the root directory of your server
2. execute that file manually per server console, wait to finish
3. edit `config.json` to your liking
4. (optional:) add your code for other url endpoints to `flask_app.py` after `entrypoint.entry()`
5. restart the server. updates happen automatically

Note that this only works on servers with persistent storage, 
this is not compatible docker and similar! 

if you serve your application locally, `flask_app.py` could look a bit like this after step 4:
```py
from Launcher.app import app
import entrypoint
from flask import send_file
import json

entrypoint.entry()

with open('static/appver.txt') as appver_file:
    app_ver = appver_file.read().strip()

@app.route('/appver')
def appver():
    return json.dumps({'success': True, 'version': app_ver}), 200


@app.route('/app_download')
def app_download():
    return send_file('../static/application.zip')

if __name__ == '__main__':
    app.run()
```

corresponding `config.json`:
```json
{
    "app":  {
        "download_url": "/app_download",
        "version_url": "/appver"
    }
}
```

##### Note: After step 2, the root folder should look more or less like this:
- `__pycache__/`
- `Launcher/`
- `res/`
- `static/`
- `checksum`
- `config.json`
- `entrypoint.py`
- `flask_app.py`
- `init.py`
- `requirements.txt`
- `sha`

### reserved endpoints
- `/download?file=launcher` - redirect to this url to let people download the launcher
##### internal use: only use when you know what you're doing
- `/download?file=application`
- `/get_version?file=launcher`
- `/get_version?file=application`

### config.json
This file appears after init in root. All fields are mandatory unless
explicitly said so.
```json
{ 
    "java_path": "P:\\ath\\to\\java.exe",
    "server": "https://www.thisserver.com",
    "launcher": {
        "name": "The name of the launcer file",
        "title": "Title displayed in the launcher",
        "icon_png": "path/relative/to/project/root/to/icon.png",
        "icon_ico": "path/relative/to/project/root/to/icon.ico"
    },
    "app":  {
        // url that returns the file in zip format
        "download_url": "https://www.url.com/application.zip",
        //url that returns: {"success": true, "version":"x.y.z"}
        "version_url": "https://www.url.com/version",
        "executable": "executable.exe"
    }
}
```
