# To ignore the escape sequences in a String, r or R is used, 
# this implies that the string is a raw string and escape sequences inside it are to be ignored.


s = r'this \\ is  hao'     # backslash
print(s)
s = r'this \n is hao'      # new line 
print(s)
s = r'this \t is hao'      # tab 
print(s)

# printing Geeks in HEX 
s = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ")
print(s)

# using raw string to ignore escape sequences: 
s = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(s)















