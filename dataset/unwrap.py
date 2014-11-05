__author__ = 'nikita_kartashov'

from sys import argv
from os import walk, path, listdir
from shutil import copy, rmtree


def relative_path(path_part):
    return path.join(path.join(path.dirname(__file__), path_part))


def unwrap(directory):
    for root, folders, files in walk(directory):
        for f in files:
            src = path.join(root, f)
            dst = path.join(directory, f)
            if not src.startswith('.') and not path.exists(dst):
                copy(src, dst)
    for f in listdir(directory):
        folder = path.join(directory, f)
        if path.isdir(folder):
            rmtree(folder)


PATHS = map(relative_path, ['downloaded-c', 'downloaded-java', 'downloaded-python'])

if __name__ == '__main__':
    if len(argv) == 1:
        for p in PATHS:
            unwrap(p)
    else:
        for arg in argv[1:]:
            unwrap(arg)




