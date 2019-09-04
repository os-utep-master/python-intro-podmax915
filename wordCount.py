import string
import sys
text = open(sys.argv[1], "r")
d = dict()

for line in text:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("","", string.punctuation))
    words = line.split(" ")
    for word in words:
        if word in d:
            d[word] = d[word]+1
        else:
            d[word] = 1

outFile = open(sys.argv[2], "w")
for key in sorted(list(d.keys())):
    s = key+" "+str(d[key])
    outFile.write(s)
    outFile.write("\n")
outFile.close()
