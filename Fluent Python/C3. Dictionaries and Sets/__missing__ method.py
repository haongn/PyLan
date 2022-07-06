d = StrKeyDict0([('2', 'two'), ('4', 'four')])

print(d['2'])
print(d['4'])
# print(d['1'])   # raise KeyError

print(d.get('2'))
print(d.get(4))
print(d.get(1, 'N/A'))
