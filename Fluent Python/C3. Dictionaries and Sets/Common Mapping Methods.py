names = ['Hao', 'Ng', 'Duy']
roll_no = [30, 55, 67]

my_dict = dict(zip(names, roll_no))
print(my_dict)
print(type(my_dict))


# common methods: 
result = my_dict.__contains__(30)          # check for keys, not values
print(result)

result = my_dict.__contains__('Hao')
print(result)














