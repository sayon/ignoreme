import sys

if len(sys.argv) ==0:
    print "Usage: python frequencies file1 file2 ...\n The result is stored in out.csv"
else:
    out = open("out.csv", "w")
    out.write(','.join(map(str, range(0, 255))) + "\n")
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
            freq = [0] * 256
            for c in f.read():
                if c != ' ' and c != '\t' and c != '\n':
                    freq[ord(c)] = freq[ord(c)] + 1
            f.close()
            out.write(','.join(map(str, freq))  + "\n")
        except IOError as e:
            print(e)
            print("Can't open file " + arg)

    out.close()