# rfind is string method. 
# return the last index where the substring is found, or -1 if no such index exists. 
# optionally restricting the search to string[beg:end]
# syntax: string.rfind(value, start, end)

txt = "hello, welcome to my world."  # the index starts at 0 
x = txt.rfind('e')
print(x)

x = txt.rfind('e', 5, 10)
print(x)

x = txt.rfind('q')   # there is no 'q' in the string
print(x)