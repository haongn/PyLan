# split a string into a list of string, after breaking the given string by the 
# specified separator. 

# syntax: str.split(separator, maxsplit)
#         maxsplit : It is a number, which tells us to split the string into maximum of 
#                    provided number of times. 
#                    If it is not provided then the default is -1 that means there is no limit.

name = 'Hao Nguyen Duy'
result = name.split()
print(result)
print(name.split(' ', 1))
print(name.split(' ', 0))

name = 'Hao.Nguyen.Duy'
result = name.split('.')
print(result)

name = 'Hao, Nguyen, Duy'
result = name.split(', ')
print(result)




