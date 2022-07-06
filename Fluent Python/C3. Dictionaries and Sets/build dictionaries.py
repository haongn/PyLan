# we can build dictionaries in several ways: 
a = dict(one = 1, two = 2, three = 3)   # dung dict method 

b = {'one': 1,           # khai bao truc tiep 
     'two': 2, 
     'three': 3}

c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # dung zip de tach key va value rieng

d = dict([('two', 2), ('one', 1), ('three', 3)])

e = dict({'three': 3, 'one': 1, 'two': 2})

print(a == b == c == d == e)
