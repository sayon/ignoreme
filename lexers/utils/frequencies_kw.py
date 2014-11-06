import os
from os.path import join
import sys
import re

def getOrDef(dic, key):
    if not key in dic.keys():
        return 0
    return dic[key]

def readList(filename):
    f = open(filename)
    res = list(map(lambda w: w.replace("\n", ""), f.readlines()))
    f.close()
    return res



out = open("out.csv", "w")
languages = readList("langs.txt")
for language in languages:
    onlyfiles = [ f for f in os.listdir(language) if os.isfile(join(language,f)) ]
    print onlyfiles

    # # caption
    # out.write(','.join(dic) + "\n")
    #
    # for arg in sys.argv[2:]:
    #     try:
    #         f = open(arg, 'r')
    #         conts = f.read()
    #         print "processing " + arg
    #         out.write(','.join(map(lambda key: str(len(re.findall(key, conts))), dic)) + "\n")
    #     except IOError as e:
    #         print(e)
    out.close()
