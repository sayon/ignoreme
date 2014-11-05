from dataset.utils.pyutils import snd

__author__ = 'nikita_kartashov'

from subprocess import call
from os import path, remove, walk

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


def download_java(directory):
    download(directory, relative_path('java.txt'))


def download_c(directory):
    download(directory, relative_path('c.txt'))


def clean(directory, extensions):
    for root, dirs, files in walk(directory):
        for f in files:
            full_path = path.join(root, f)
            if path.isfile(full_path) \
                    and not path.isdir(full_path) \
                    and not file_fits(full_path, extensions):
                print(full_path)
                # remove(path.join(root, dirs, f))


def file_fits(f, extensions):
    separated_file = f.split('.')
    return len(separated_file) > 1 and snd(separated_file) in extensions


if __name__ == '__main__':

    # download('lolololol', path.join(REPO_PATH, 'lol.txt'))
    clean('lolololol', [])