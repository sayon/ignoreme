__author__ = 'nikita_kartashov'

from os import path
from itertools import chain


def fst(l):
    return l[0]


def snd(l):
    return l[1]


def last(l):
    return l[len(l) - 1]


def relative_path(path_part, relative=__file__):
    return path.join(path.join(path.dirname(path.abspath(relative)), path_part))


def dict_to_list(d, order):
    if order:
        res = []
        for k in order:
            e = d.get(k)
            if e is None:
                e = d.get(str(k))
            res.append(float(e))
        return res
    else:
        return list(d.itervalues())


def flatten(l):
    return list(chain.from_iterable(l))

