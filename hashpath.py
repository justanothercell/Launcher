import hashlib
import os
from os.path import normpath, isdir, isfile, dirname, basename, exists as path_exists, join as path_join
from os import walk


def path_checksum(paths):
    def _update_checksum(checksum, dname, filenames):
        for filename in sorted(filenames):
            path = path_join(dname, filename)
            checksum.update(path.encode('utf-8'))
            print(path)
            fh = open(path, 'rb')
            while 1:
                buf = fh.read(4096)
                if not buf: break
                checksum.update(buf)
            fh.close()

    chksum = hashlib.sha1()

    for path in sorted([normpath(os.getcwd() + '/' + f) for f in paths]):
        print('p', path)
        if path_exists(path):
            if isdir(path):
                for bdir, dirs, files in walk(path):
                    _update_checksum(chksum, bdir, files)
            elif isfile(path):
                _update_checksum(chksum, dirname(path), basename(path))

    return chksum.hexdigest()