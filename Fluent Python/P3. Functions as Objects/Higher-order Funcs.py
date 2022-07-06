fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

# sort the list in the increasing length of the word: 
print(sorted(fruits, key = len))    # higher-order function 


def reverse(word): 
    return word[::-1]


if __name__ == '__main__':
    print(reverse('testing'))
    print(sorted(fruits, key = reverse))

    















