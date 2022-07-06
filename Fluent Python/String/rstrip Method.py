# rstrip(): returns a copy of the string with trailing characters removed (based on the 
#           string argument passed). If no argument is passed, it removes trailing spaces.   
# syntax: string.rstrip([char])
#         char - optional - a string specified the set of characters to be removed. 
#         return a copy of the string with trailing characters is stripped 

# trailing characters: characters at the end of a string. 

# chú ý: sẽ bắt đầu cắt từ bên phải, khi gặp một ký tự khác các 
# ký tự cần cắt thì method sẽ lập tức dừng lại.


string = 'geekssss'
print(string.rstrip('s'))  # remove 's' character from right 

string = '    for          '
print('geeks' + string.rstrip() + ' geeks')    # leading whitespaces were removed 

string = 'geeks for geeks'
print(string.rstrip('ek'))

string = 'geeks for geeks'
print(string.rstrip('eks'))

string = 'geeks for geeks'
print(string.rstrip('sek'))   # the same as above

txt = 'banana,,,,ssqqqww....'
print(txt.rstrip(',.qsw'))
print(txt.rstrip('q,w.s'))