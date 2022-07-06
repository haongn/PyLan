# Type Specifying: 

# More parameters can be included within the curly braces of our syntax. 
# syntax: {field_name: conversion}
#         conversion: refers to the conversion code of the data type

# Some another useful Type Specifying:
# %u: unsigned decimal integer
# %o: octal integer
# f – floating point display
# b – binary
# o – octal
# %x – hexadecimal with lowercase letters after 9
# %X– hexadecimal with uppercase letters after 9
# e – exponent notation


# %s - string conversion: 
print('%20s'  % ('geeksforgeeks'))     # can le ve ben phai
print('%-20s' % ('interngeeks'))       # can le ve ben trai 
print('%.5s' % ('interngeeks'))        # chi lay 5 ky tu dau tien


print('The {} of 100 is: {:o}'.format('octal', 100))   # convert integer to octal 
print('The {} of 100 is: {:b}'.format('binary', 100))  # convert integer to binary

print("{0:4}, is the computer science portal for {1:8}!".format("GeeksforGeeks", "geeks"))
print("It is {0:5} degrees outside !".format(40))      # numbers are left aligned by default
print("{0:4} was founded in {1:16}!".format("GeeksforGeeks", 2009))
print("{0:^16} was founded in {1:<6}!".format("GeeksforGeeks", 2009))
print("{:*^20}".format("Geeks"))
print("{:*^20s}".format("Geeks"))
print('{:-^20s}'.format('Geeks'))














