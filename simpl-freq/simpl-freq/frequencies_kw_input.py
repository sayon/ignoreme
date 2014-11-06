import re
import sys

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
    return count


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("usage: progname dictionary_file file_to_count_kws")
    else:
        print countKeywords(readList(sys.argv[1]), sys.argv[2])