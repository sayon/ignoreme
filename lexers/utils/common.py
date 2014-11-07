import os
from os.path import join
from re import findall
import mmap

__author__ = 'sayon'



def countlines(f):
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
        lines += 1
    return lines


def quote(s):
    s = str(s)
    if ("\"" in s): s = s.replace("\"", "\"\"")
    if ( "," in s or ";" in s):
        return "\"" + s + "\""
    else:
        return s


def goodChar(c):
    n = ord(c)
    return (n >=33 and n <= 47 ) or (n >= 58 and n <= 64 ) or (n >= 91 and n <= 96) or (n >= 123 and n <= 126)

def goodCharsList():
    return filter(lambda c: goodChar(chr(c)),range(0, 255))


def readList(filename):
    f = open(filename)
    res = list(map(lambda w: w.replace("\n", ""), f.readlines()))
    f.close()
    return res

def keywordsFromDirectory(dirname):
    files = [f for f in os.listdir(dirname) if os.path.isfile(join(dirname, f))]
    def sanitize(fname):
        kw = str(fname).find("_keywords.txt")
        if kw != -1: return fname[0:kw]
        ext = str(fname).find(".txt")
        if ext != -1: return fname[0:ext]
        return fname

    return dict([(sanitize(filename), readList(filename)) for filename in files])

def keywordsAndSymbolsFrequencies(kws, contents):
    length_total = 0
    features = dict()
    for kw in kws:
        features[kw] = len(findall(kw, contents))
    for code in goodCharsList():
        features[code] = 0

    for sym in contents:
        if goodChar(sym):
            features[ord(sym)] = features.get(ord(sym), 0) + 1
            length_total += 1

    for w in features.keys():
        if length_total != 0:
            features[w] /= 1. * length_total

    return features