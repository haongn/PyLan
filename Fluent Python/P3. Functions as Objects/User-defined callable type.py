import random


class BingoCage: 
    """A BingoCase does one thing: picks items from a shuffled list.
    An instance is built from any iterable, and stores an internal list of items, in random order. 
    Calling the instance pops an item."""

    def __init__(self, items):        # accept any iterable 
        self._items = list(items)     # turn items into a list 
        random.shuffle(self._items)   # shuffle the list 

    def pick(self): 
        try: 
            return self._items.pop()  # take the last element from the list 
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):     # shortcut to call pick() method 
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCage(range(5))
    result = bingo.pick()
    print(result)

    print(bingo())
    print(bingo())
    print(bingo())
    print(bingo())
    
    # print(bingo())

    print(callable(bingo))
    print(callable(BingoCage))




    
















