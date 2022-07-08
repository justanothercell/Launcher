import shutil
import os
import build_launcher

if __name__ == '__main__':
    shutil.copy('entrypoint.py', '../entrypoint.py')
    build_launcher.build()
    os.system('python ../entrypoint.py')