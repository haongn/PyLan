# handling missing keys with setdefault method 
# we show that dict.get is not the best way to handle a missing key.

import sys
import re 


WORD_RE = re.compile('w+')

index = {}
with open(sys.argv[1], encoding = 'utf8') as fp: 
    for line_no, line in enumerate(fp, 1): 
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # this is ugly; code like this to make a point 
            occurences = index.get(word, [])
            occurences.append(location)
            index[word] = occurences

# print in alphabetical order: 
for word in sorted(index, key = str.upper):  
    print(word, index[word])
        



        


