import hashlib
import os
from os.path import normpath, isdir, isfile, dirname, basename, exists as path_exists, join as path_join
from os import walk


def path_checksum(paths):
    def _update_checksum(checksum, dirname, filenames):
        for filename in sorted(filenames):
            path = path_join(dirname, filename)
            if isdir(path):
                for bdir, dirs, files in walk(path):
                    for d in dirs:
                        _update_checksum(chksum, bdir, d)
                    for f in files:
                        _update_checksum(chksum, bdir, f)
            elif isfile(path):
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
        print(path_exists(path), isdir(path), isfile(path))
        if path_exists(path):
            if isdir(path):
                for bdir, dirs, files in walk(path):
                    for d in dirs:
                        _update_checksum(chksum, bdir, d)
                    for f in files:
                        _update_checksum(chksum, bdir, f)
            elif isfile(path):
                _update_checksum(chksum, dirname(path), basename(path))

    return chksum.hexdigest()