import os
from os.path import join
import re
import mmap

def quote(s):
    s = str(s)
    if ("\"" in s): s = s.replace("\"", "\"\"")
    if ( "," in s or ";" in s):
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
    print "Language: " , language
    files = [ f for f in os.listdir(language) if os.path.isfile(join(language,f)) ]
    # print "Files: ", files

    kws = dict()
    for kw in readList(language+"_keywords.txt"):
        kws[kw] = 0


    for filename in files:
        features = dict()
        file = open(language + "/" + filename, 'r')
        contents = file.read()
        length_total = 0
        for kw in kws.keys():
            features[kw] = len( re.findall(kw, contents ))
        for sym in contents:
            if sym != ' ' and sym != '\t' and sym != '\n':
                features[sym] = getOrZero(features, sym ) + 1
                length_total += 1

        for w in features.keys():
            if length_total != 0 : features[w] = features[w] * 1. / length_total
        file.close()
        results[filename] = (features, language)


allfeatures = reduce(lambda x, y: x | set(y[0].keys()) , results.values(), set())

out = open("out.csv", "w")

out.write("name," + ",".join(map(quote, allfeatures)) + "\n")

for entry in results.keys():
    out.write(results[entry][1])
    for feature in allfeatures:
        if '\0' not in feature:
            out.write("," + str(getOrZero(results[entry][0], feature)))
    out.write("\n")


out.close()

