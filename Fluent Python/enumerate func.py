# Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. 
# This enumerated object can then be used directly 
# for loops or converted into a list of tuples using the list() method.

# Hieu don gian la enumerate se gan them mot iterable object chua index vao voi iterable object 
# ban dau, roi sau do zip hai iterable object voi nhau. 

# syntax: enumerate(iterable, start = 0)
#         start: index value from which the counter is to be started, by default it is 0. 

l1 = ['eat', 'sleep', 'repeat']
s1 = 'geek'

# creating enumerate objects: 
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print(type(obj1))                   # enumerate object
print(list(obj1), end = '\n\n')     # print elements with corresponding index in the original list

print(list(enumerate(s1)), end = '\n\n')          

# changing start index from 0 to 2: 
print(list(enumerate(s1, 2)), end = '\n\n')


# ex2: 
l1 = ['eat', 'sleep', 'repeat']

# printing the tuples in object directly: 
for ele in enumerate(l1): 
    print(ele)       # print tuple (element + its index)

# changing index and printing separately (element + its index): 
for count, ele in enumerate(l1, 100): 
    print(count, ele)

# getting desired output from tuple: 
for count, ele in enumerate(l1): 
    print(count)
    print(ele)





