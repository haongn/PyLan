def factorial(n): 
    """Returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(42))
    print(factorial.__doc__)   # generate the help text of an object 
    print(type(factorial))
    print(help(factorial))

    # use function through a different name: 
    fact = factorial
    print(fact)                # print location of the function at memory 
    print(fact(5)) 

    # pass function as argument: 
    print(map(factorial, range(11)))    # return map object (an iterable)
    print(list(map(fact, range(11))))   # return a list 

    






















