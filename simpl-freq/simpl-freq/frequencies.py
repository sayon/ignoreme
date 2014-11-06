import sys


def getOrDef(dic, key):
    if not key in dic.keys():
        return 0
    return dic[key]


if len(sys.argv) ==0:
    print "Usage: python frequencies file1 file2 ...\n The result is stored in out.csv"
else:
    out = open("out.csv", "w")
    keys = []

    encountered = set()
    freqs = []
    for arg in sys.argv[2:]:
        print "processing " + arg
        try:
            f = open(arg, 'r')
            freq = dict()

            conts =  f.read()
            print("Contents:" + conts + "\n")
            f.close()

            #character frequencies
            for c in conts:
                if c != ' ' and c != '\t' and c != '\n':
                    encountered.add(c)
                    freq[c] = getOrDef(freq,c) + 1

            for w in filter(None, ''.join(conts).split(' ')):
                encountered.add(w)
                freq[w] = getOrDef(freq, w) + 1

            map(lambda key: str(len(re.findall(key, conts))), dic)
            freqs.append(freq)

        except IOError as e:
            print(e)
            print("Can't open file " + arg)


    out.write(','.join(encountered) + "\n")
    for i in xrange(0, len(sys.argv)-1):
        s = ""
        for w in encountered:
            s = s + str(getOrDef(freqs[i], w)) + ","
        out.write(s[0:-1] + "\n")

    #     out.write(','.join(map(lambda w : getOrDef(freqs[i], w),encountered)) + '\n')

    out.close()