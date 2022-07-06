# formatting of integers: 
s = '{0:b}'.format(16)          # 0: positional formatting, b: binary mode 
print('Binary representation of 16: ', end = '')
print(s)

# formatting of floats: 
s = '{0:e}'.format(165.6458)    # 0: positional formatting, e: scientific mode
print('\nExponent representation of 165.6458: ', end = '')   # ky hieu khoa hoc
print(s)

# rounding of integers: 
s = '{0:.2f}'.format(1/6)       # 0: positional formatting, f: float mode 
print('\nOne-Sixth is: ', end = '')
print(s)







