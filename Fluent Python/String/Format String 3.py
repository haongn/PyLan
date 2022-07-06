# string alignment:

s = '|{:<10}|{:^10}|{:>10}|'.format('Geeks', 'for', 'Geeks')  # trai: max 10, giua: max 10, phai: max 10
print('Left, center and right alignment with Formatting:')
print(s)

s = '{0:^16} was founded in {1:<7}!'.format('GeeksforGeeks', 2009) # 0, 1: positional formatting
print(s)













