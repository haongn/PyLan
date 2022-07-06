# f-string: formatted string literals 
# The idea behind f-strings is to make string interpolation simpler. 
# To create an f-string, prefix the string with the letter “ f ”. 
# The string itself can be formatted in much the same way that you would with str.format(). 
# F-strings provide a concise and convenient way to embed python expressions inside string 
# literals for formatting.

# Note : F-strings are faster than the two most commonly used string formatting mechanisms, 
# which are % formatting and str.format(). 


val = 'Geeks'
print(f'{val}for{val} is a portal for {val}.')

name = 'Hao'D:

age = 22
print(f'Hello, my name is {name} and I\'m {age} years old.')

import datetime 

today = datetime.datetime.today()
print(f'{today:%B %d, %Y}')   # f-string with formatting 

# Nhận xét: Để tạo f-string, tạo một biến chứa dữ liệu kiểu string. Sau đó, tạo một f-string 
# (bắt đầu bằng f) và chứa tên biến chứa kiểu dữ liệu string cần thay thế.