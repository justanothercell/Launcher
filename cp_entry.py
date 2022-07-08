import shutil
import os

if __name__ == '__main__':
    shutil.copy('entrypoint.py', '../entrypoint.py')
    os.system('python ../entrypoint.py')