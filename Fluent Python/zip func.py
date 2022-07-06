# zip() method: takes iterable/containers and returns a single interator object, 
#               having mapped values from all the containers. 
# It is used to map the similar index of multiple containers so that they can be used 
# just using a single entity. 

# syntax: zip(*iterable: iterables/containers) -> return a single iterator object.
# => de hien thi duoc DL ra man hinh, can dung them cac method khac de chuyen doi ve dict.

# ex1: python zip two lists: 
name = ['Hao', 'Ng', 'Duy']
roll_no = [4, 1, 3, 2]

mapped = zip(name, roll_no)    # using zip() to map values
print(type(mapped))
print(mapped)         # location of zip object in memory

print(set(mapped))    # return dictionary 


# ex2: python zip enumerate: 
names = ['Hao', 'Ng', 'Duy']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)): 
    print(i, name, age)


# ex3: python zip() dictionaries:
stocks = ['FB', 'GG', 'HW']
prices = [50, 20, 30]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print(new_dict)












