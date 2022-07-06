# rindex() is the string method. 
# rindex() is almost similar to rfind(), except that it return an error if there is no match found. 

txt = "hello, welcome to my world."  # the index starts at 0 
x = txt.rindex('e')
print(x)

x = txt.rindex('e', 5, 10)
print(x)

x = txt.rindex('q')   # there is no 'q' in the string
print(x)