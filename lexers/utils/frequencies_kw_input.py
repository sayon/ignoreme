import re
import sys
from lexers.utils.common import keywordsAndSymbolsFrequencies


def readList(filename):
    f = open(filename)
    res = list(map(lambda w: w.replace("\n", ""), f.readlines()))
    f.close()
    return res

def countKeywords(kws, filename):
    count = dict()
    for kw in kws:
        count[kw] = 0
    with open(filename, 'r') as file:
        contents = file.read()
        for kw in kws:
            count[kw] = len(re.findall(kw, contents))
        total = sum(count.values()) * 1.0
        for kw in kws:
            count[kw] /= total

    return count



def countKeywordsAndSymbols(kws, filename):
    with open(filename, 'r') as file:
        return keywordsAndSymbolsFrequencies(kws, file.read())


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("usage: progname dictionary_file file_to_count_kws")
    else:
        print countKeywordsAndSymbols(readList(sys.argv[1]), sys.argv[2])