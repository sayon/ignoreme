import sys
import re


def getOrDef(dic, key):
    if not key in dic.keys():
        return 0
    return dic[key]


def loadDict(filename):
    f = open(filename)
    res = set(map(lambda w: w.replace("\n", ""), f.readlines()))
    f.close()
    return res


if len(sys.argv) == 0:
    print "Usage: python frequencies_kw dictionary_file file1 file2 ...\n The result is stored in out.csv"
else:
    out = open("out.csv", "w")

    dic = loadDict(sys.argv[1])

    # caption
    out.write(','.join(dic) + "\n")

    for arg in sys.argv[2:]:
        try:
            f = open(arg, 'r')
            conts = f.read()
            print "processing " + arg
            out.write(','.join(map(lambda key: str(len(re.findall(key, conts))), dic)) + "\n")
        except IOError as e:
            print(e)
    out.close()
