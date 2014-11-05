from dataset.utils.pyutils import snd

__author__ = 'nikita_kartashov'

from subprocess import call
from os import path, remove, walk
from logging import info, basicConfig

GIT_STRING_TEMPLATE = ['git', 'clone']

REPO_PATH = path.join(path.dirname(__file__), 'repos')


def relative_path(repos):
    return path.join(REPO_PATH, repos)


def download(directory, repos):
    with open(repos) as repo_file:
        for repo in repo_file.readlines():
            call(GIT_STRING_TEMPLATE + [repo, directory])


def download_python(directory):
    download(directory, relative_path('python.txt'))
    clean(directory, ['py'])


def download_java(directory):
    download(directory, relative_path('java.txt'))
    clean(directory, ['java'])


def download_c(directory):
    download(directory, relative_path('c.txt'))
    clean(directory, ['c'])


def clean(directory, extensions):
    for root, dirs, files in walk(directory):
        for f in files:
            full_path = path.join(root, f)
            if path.isfile(full_path) \
                    and not path.isdir(full_path) \
                    and not file_fits(full_path, extensions):
                info('Removed {0}'.format(full_path))
                remove(full_path)


def file_fits(f, extensions):
    separated_file = f.split('.')
    return len(separated_file) > 1 and snd(separated_file) in extensions


if __name__ == '__main__':
    basicConfig(filename='download_logging.log')
    download('lolololol', path.join(REPO_PATH, 'lol.txt'))
    clean('lolololol', ['py'])