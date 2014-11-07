import os
from os.path import join
import re
import mmap

def quote(s):
    s = str(s)
    if "\"" in s: s = s.replace("\"", "\"\"")
    if "," in s or ";" in s:
        return "\"" + s + "\""
    else:
        return s

def getOrZero(dic, key):
    if not key in dic.keys():
        return 0
    return dic[key]


def countlines(f):
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
        lines += 1
    return lines

def readList(filename):
    f = open(filename)
    res = list(map(lambda w: w.replace("\n", ""), f.readlines()))
    f.close()
    return res


languages = readList("langs.txt")
results = dict()

for language in languages:
    print "Language: ", language
    files = [f for f in os.listdir(language) if os.path.isfile(join(language, f))]

    kws = dict()
    for kw in readList(language + "_keywords.txt"):
        kws[kw] = 0

    for filename in files:
        with open(language + "/" + filename, 'r') as file:
            print "file: " + filename
            contents = file.read().replace(" ", "").replace("\t", "").replace("\n", "")
            length_total = len(contents) * 1.

            keywords = dict()
            symbols = dict()
            doubles = dict()

            for kw in kws.keys():
                keywords[kw] = len(re.findall(kw, contents))

            for sym in contents:
                symbols[sym] = getOrZero(symbols, sym) + 1

            for i in xrange(0, len(contents)-2):
                double = contents[i:i+2]
                doubles[double] = getOrZero(doubles, double) + 1

            if length_total != 0:
                for double in doubles:
                    doubles[double] /= length_total
                for sym in symbols:
                    symbols[sym] /= length_total
                for kw in keywords:
                    keywords[kw] /= length_total

            features = dict(keywords, **symbols)
            features = dict(doubles, **features)

        results[filename] = (features, language)

allfeatures = reduce(lambda x, y: x | set(y[0].keys()), results.values(), set())
allfeatures = filter(lambda x: not '\0' in x, allfeatures)

out = open("out.csv", "w")

out.write("name," + ",".join(map(quote, allfeatures)) + "\n")

for entry in results.keys():
    out.write(results[entry][1])
    for feature in allfeatures:
            out.write("," + str(getOrZero(results[entry][0], feature)))
    out.write("\n")

out.close()

