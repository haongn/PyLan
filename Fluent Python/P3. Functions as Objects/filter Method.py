# The filter() method filters the given sequence with the help of a function that 
# tests each element in the sequence to be true or not.
# syn: filter(func, sequence): return an iterator that is already filtered. 

def fun(variable): 
    """Test the variable if it is one of the 5 characters."""
    letters = ['a', 'e', 'i', 'o', 'u']

    if variable in letters:
        return True
    else: 
        return False


if __name__ == '__main__':
    sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
    filtered = filter(fun, sequence)   # return filter object 
    print(filtered)    # filter object at memory 

    for s in filtered:
        print(s)



# It is normally used with Lambda functions to separate list, tuple, or sets

# a list containing both even and odd numbers: 
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list: 
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
result = filter(lambda x: x % 2, seq)   # same as above (default)
print(list(result))

# result contains even numbers of the list: 
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))




















