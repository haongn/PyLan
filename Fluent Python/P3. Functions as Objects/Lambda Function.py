# cu phap chung cua ham lambda: 
# lambda: <input value>: <output value (co the thoa man mot dieu kien nào do)>


a = [0, 3, 5, 2, 9, 4, 15, 7, 1, 6]

result = filter(lambda x: x > 6, a)
print(list(result))

# mapping: 
result = map(lambda x: x + 10, a)
print(list(result))