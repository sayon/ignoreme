import os
from os.path import join

from common import readList,  quote, keywordsAndSymbolsFrequencies


languages = readList("langs.txt")
results = dict()

for language in languages:
    print "Language: ", language
    files = [f for f in os.listdir(language) if os.path.isfile(join(language, f))]
    fileno = 1
    kws = readList(language + "_keywords.txt")
    for filename in files:
        if fileno % 10 == 0:
            print filename, " file ", fileno, " out of ", len(files)
        fileno += 1

        with open(language + "/" + filename, 'r') as file:
             features = keywordsAndSymbolsFrequencies(kws, file.read())

        results[filename] = (features, language)

allFeatures = reduce(lambda x, y: x | set(y[0].keys()), results.values(), set())

with open("out_nonalpha.csv", "w") as out:
    out.write("name," + ",".join(map(quote, allFeatures)) + "\n")
    for entry in results.keys():
        out.write(results[entry][1])
        for feature in allFeatures:
                out.write("," + str( results[entry][0].get(feature, 0)))
        out.write("\n")
