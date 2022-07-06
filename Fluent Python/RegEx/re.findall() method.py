# syntax: re.findall(Regex, string): 
#         regex: the text pattern to be searched 
#         string: the string to be applied the search    

# goal: used to search given text data according to the provided patterns.

import re 


s = 'black, blue and brown'
pattern = r'bl\w+'        # start with 'bl' + followed by one or more word characters
matches = re.findall(pattern, s)
print(matches)      # return a list of strings that matches the whole pattern 

# pattern that has a single group:
s = 'black, blue and brown'
pattern = r'bl(\w+)'     # only return the characters in () (if exist)
matches = re.findall(pattern, s)
print(matches)

# pattern that has multiple groups: 
s = 'black, blue and brown'
pattern = r'(bl(\w+))'       # return all the matching groups (in form of a list of tuples)
matches = re.findall(pattern, s)
print(matches)

# ignore the the character cases (tuc match ca chu hoa va chu thuong): 
s = 'Black, blue and brown'
pattern = r'(bl(\w+))'
matches = re.findall(pattern, s, re.IGNORECASE)
print(matches)






























