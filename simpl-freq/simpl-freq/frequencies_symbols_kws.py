import sys
import re

def quote(s):
    return "\"" + str(s) + "\""

def loadDict(filename):
    f = open(filename)
    res = set(map(lambda w: w.replace("\n", ""), f.readlines()))
    f.close()
    return res


def getOrDef(dic, key):
    if not key in dic.keys():
        return 0
    return dic[key]


if len(sys.argv) ==0:
    print "Usage: python frequencies file1 file2 ...\n The result is stored in out.csv"
else:
    out = open("out.csv", "w")
    keys = []
    dic = loadDict(sys.argv[1])


    encountered = set(dic)
    freqs = []
    for arg in sys.argv[2:]:
        print "processing " + arg
        try:
            f = open(arg, 'r')
            freq = dict()

            conts =  f.read()
            # print("Contents:" + conts + "\n")
            f.close()

            #character frequencies
            for c in conts:
                if c != ' ' and c != '\t' and c != '\n':
                    encountered.add(c)
                    freq[c] = getOrDef(freq,c) + 1

            for key in dic:
                freq[key] =  len(re.findall(key, conts))
            freqs.append(freq)

        except IOError as e:
            print(e)
            print("Can't open file " + arg)


    out.write(",".join(map(quote, encountered)) + "\n")
    for i in xrange(0, len(sys.argv)-2):
        s = ""
        for w in encountered:
            elem = str(getOrDef(freqs[i], w))
            s = s + elem + ","
        out.write(s[0:-1] + "\n")

    #     out.write(','.join(map(lambda w : getOrDef(freqs[i], w),encountered)) + '\n')

    out.close()