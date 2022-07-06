# re.finditer: return an iterator yielding MatchObject instances over all non-overlapping 
# matches for the RE pattern in string. The string is scanned left-to-right, and matches are 
# returned in the order found. Empty matches are included in the result. 

# The re.finditer() works exactly the same as the re.findall() method except it returns 
# an iterator yielding match objects matching the regex pattern in a string instead of a list.

# It scans the string from left to right, and matches are returned in the iterator form. 
# Later, we can use this iterator object to extract all matches.

# In simple words, finditer() returns an iterator over MatchObject objects.

# => hieu don gian la luc nay de in ra man hinh, ra can dung lap for voi match object. 
# luc nay, ban chat la ra su dung ham yield de lay ra tung match mot. 

# But why use finditer()?
# In some scenarios, the number of matches is high, and you could risk filling up your memory 
# by loading them all using findall(). Instead of that using the finditer(), you can get all 
# possible matches in the form of an iterator object, which will improve performance.

# It means, finditer() returns a callable object which will load results in memory when called.

import re 


s = """Emma is a basketball player who was born on June 17, 1993. She played 112 matches with 
    a scoring average of 26.12 points per game. Her weight is 51 kg."""
pattern = r'\d{2}'   # find all two consecutive digits 
matches = re.finditer(pattern, s)

# print all match object: 
for match in matches: 
    print(match)             # print all re.Match object 
    print(match.group())     # extract each matching number 


# ex2: 
import re 


s1 = 'Blue Berries'
pattern = 'Blue Berries'
for match in re.finditer(pattern, s1): 
    s = match.start()
    e = match.end()
    print('String match "%s" at %d:%d' % (s1[s:e], s, e))









