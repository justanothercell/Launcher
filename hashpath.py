import hashlib
import os
from os.path import normpath, isdir, isfile, dirname, basename, exists as path_exists, join as path_join
from os import walk


def path_checksum(paths):
    def _update_checksum(checksum, dirname, filenames):
        for filename in sorted(filenames):
            path = path_join(dirname, filename)
            if isfile(path):
                checksum.update(path)
                print(path)
                fh = open(path, 'rb')
                while 1:
                    buf = fh.read(4096)
                    if not buf: break
                    checksum.update(buf)
                fh.close()

    chksum = hashlib.sha1()

    for path in sorted([normpath(f) for f in paths]):
        print('is?', path, path_exists(path), os.getcwd())
        if path_exists(path):
            if isdir(path):
                walk(path, _update_checksum, chksum)
            elif isfile(path):
                _update_checksum(chksum, dirname(path), basename(path))

    return chksum.hexdigest()