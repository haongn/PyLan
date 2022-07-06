# default order:
s = '{} {} {}'.format('Geeks', 'for', 'Life')
print(s)

# positional formatting: 
s = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print('\n' + s)

# keyword formatting: 
s = '{l} {f} {g}'.format(g = 'Geeks', f = 'For', l = 'Life')
print('\n' + s)






