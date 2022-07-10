import entrypoint
# order is important!
entrypoint.entry()
from Launcher.app import app

if __name__ == '__main__':
    app.run()