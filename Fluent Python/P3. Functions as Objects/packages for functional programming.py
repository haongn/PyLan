# operator
# functools 

from functools import reduce

def fact(n): 
    return reduce(lambda a, b: a * b, range(1, n + 1))

# rewrite above function: 
from functools import reduce 
from operator import mul, add

def fact(n): 
    return reduce(mul, range(1, n + 1))

def summation(n): 
    return reduce(add, range(1, n + 1))


if __name__ == '__main__':
    print(fact(10))
    print(summation(10)) 


# functions to pick items from a sequences/ read attributes from objects: itemgetter, attrgetter

# itemgetter: functions to pick items from a sequences
# vi dụ: sorting a list of tuples by the value of index 1. 
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

from operator import itemgetter

for city in sorted(metro_data, key = itemgetter(1)):   # itemgetter(1) = lambda fields: fields[1]
    print(city)      







