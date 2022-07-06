# unzip(): converting the zipped values back to the individual self as they were. 
# This is done with the help of "*" operator. 

name = ['Hao', 'Ng', 'Duy', 'Minh']
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values: 
mapped = zip(name, roll_no, marks)    # return a single iterator object 

# converting values to print as a list: 
mapped = list(mapped)                 # convert iterator object into list

# print resultant values: 
print(mapped)
print()

# unzip values: 
namz, roll_noz, marksz = zip(*mapped)     

print(namz)
print(roll_noz)
print(marksz)
print()


# Practical Applications: 
players = ['Hao', 'Ng', 'Duy', 'Minh', 'Phong', 'Hoang']
scores = [100, 15, 17, 28, 43]

for pl, sc in zip(players, scores): 
    print('Player: %s      Score: %d' % (pl, sc))

