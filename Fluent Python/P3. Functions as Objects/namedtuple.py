# from collections import namedtuple


# namedtuple is a type of container, much like dictionary. 
# like dictionaries, it contains key that are hashed to a particular value. 
# however, it supports both access from key-value and iteration, which is a feature that dict 
# dont have.  

# access operations:
# 1. access by index 
# 2. access by keyname 
# 3. access by getattr(): getattr(<namedtuple>, <key value>)

from collections import namedtuple

# declare namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# adding value: 
S = Student('Hao', '19', '20092000')

# access using index: 
print('The Student age using index:', S[1])
print(S.age)

# access using name: 
print('The Student name using keyname:', S.name)

# access using getattr(): 
print(getattr(S, 'DOB'))


# conversion operations: 
# 1. make(): 
# 2. _asdict(): 
# 3. **