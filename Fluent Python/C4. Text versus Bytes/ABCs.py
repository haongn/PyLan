# ABCs: abstract base class

# hasattr/isinstance (methods): check whether the input conforms to a particular identity

import abc

my_dict = {}
# result = isinstance(my_dict, abc.Mapping)    # there is no attri named Mapping
# print(result)

result = isinstance(my_dict, dict)
print(result)

result = isinstance(my_dict, set)
print(result)


# ABCMeta metaclass provides a method called register method that can be invoked by its instance. 
# By using this register method, 
# any abstract base class can become an ancestor of any arbitrary concrete class.

import abc 


class AbstractClass(metaclass = abc.ABCMeta): 
    def abstractfunc(self): 
        return None 

print(AbstractClass.register(dict))  # dict identifies itself as a subclass of AbstractClass. 

# check: 
print(issubclass(dict, AbstractClass))

print(isinstance([], (list, tuple)))


import abc 


class MySequence(metaclass = abc.ABCMeta): 
    pass 

MySequence.register(list)    # become an ancestor of a concrete class (list)
MySequence.register(tuple)

a = [1, 2, 3]                # an instance of list class 
b = ('x', 'y', 'z')          # an instance of tuple class

print('List instance:', isinstance(a, MySequence))  # check if a is a instance of MySequence class
print('Tuple instance:', isinstance(b, MySequence))
print('Object instance:', isinstance(object(), MySequence))


class Foo: 
    pass 

x = Foo()
print(isinstance(x, Foo))



import abc 


class MySequence(metaclass = abc.ABCMeta): 
    pass 

class CustomListLikeObjCls(object): 
    pass 

MySequence.register(CustomListLikeObjCls)
print(issubclass(CustomListLikeObjCls, MySequence))





