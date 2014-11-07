__author__ = 'nikita_kartashov'

from os import path


def fst(l):
    return l[0]


def snd(l):
    return l[1]


def last(l):
    return l[len(l) - 1]


def relative_path(path_part, relative=__file__):
    return path.join(path.join(path.dirname(path.abspath(relative)), path_part))
