# A Tuple is a collection of Python objects separated by commas. 
# In someways a tuple is similar to a list in terms of indexing, nested objects and repetition.
# But a tuple is immutable unlike lists which are mutable.

# tuple co the chua data type bat ky, giong list.


# create an empty tuple: 
empty_tuple = ()
print(empty_tuple)


# creating non-empty tuple: 
tup = 'python', 'geeks'       # one way of creation 
print(tup)

tup = ('python', 'geeks')     # another way for doing the same 
print(tup)

# Note: In case your generating a tuple with a single element, 
# make sure to add a comma after the element.
tup = ('hello', )     # this is tuple 
print(tup)

tup = ('hello')       # not a tuple 
print(tup)

# concatenation of tuples: 
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
tuple3 = tuple1 + tuple2       # concanating the above two 
print(tuple3)







