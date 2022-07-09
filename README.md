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

##### Note: After step 3, the root folder should look a bit like this:
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

### relevant endpoints
`/download?file=launcher` - redirect to this url to let people download the launcher
`/download?file=application` - used internally, only use if necessary, e.g. launcher doesn't work


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
        "version_url": "https://www.url.com/version"
    }
}
```
