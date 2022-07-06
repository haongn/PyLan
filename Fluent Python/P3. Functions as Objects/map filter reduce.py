def factorial(n): 
    """Returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    fact = factorial 
    print(list(map(fact, range(6))))     # map 
    print([fact(n) for n in range(6)])   # list comprehension 

    result = list(map(factorial, filter(lambda n: n % 2, range(6))))
    print(result)
    result = [factorial(n) for n in range(6) if n % 2]  # list comprehension 
    print(result)


# sum of integers up to 99 performed with reduce and sum
from functools import reduce 
from operator import add 

result = reduce(add, range(100))
print(result)

# same task using sum, import or adding function not needed: 
result = sum(range(100))
print(result)



















