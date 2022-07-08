import shutil
import os
import build_launcher

if __name__ == '__main__':
    print('Updating launcher...')
    print('Copying entrypoint')
    shutil.copy('entrypoint.py', '../entrypoint.py')
    print()
    build_launcher.build()
    print('Relaunching')
    os.system('../entrypoint.py')