# The reduce(fun,seq) function is used to apply a particular function passed in its argument to 
# all of the list elements mentioned in the sequence passed along.This function is defined 
# in “functools” module.

# Working :  

# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.


import functools


lis = [1, 3, 5, 6, 2]

# using reduce to compute the sum of the list: 
result = functools.reduce(lambda a, b: a + b, lis)
print(result)

# using reduce to compute maximum element of the list: 
maximum = functools.reduce(lambda a, b: a if a > b else b, lis)
print(maximum)


# reduce() can also be combined with operator functions to achieve the similar functionality 
# as with lambda functions and makes the code more readable.
from functools import reduce
from operator import add, mul

lis = [1, 3, 5, 6, 2]

# using reduce to compute sum: 
result = reduce(add, lis)
print(result)

# using reduce to compute product: 
result = reduce(mul, lis)
print(result)

# using add to concatenate string: 
strg = reduce(add, ['geeks', 'for', 'geeks'])
print(strg)

# NX: reduce tuong ung voi mot vong lap for, va khong the dung list compre thay the duoc. 
# vi ban chat cua list compre la ap dung ham len tung phan tu trong iterable, nen ket qua 
# khong the ket noi voi nhau duoc. 















