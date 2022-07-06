def myFun(*argv): 
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'Goodbye')
print()

# Mot so luu y ve *argv: 
# - *argv co the dung dau, giua hoac dung sau (trong ds cac tham so) deu duoc. 
# - *argv la mot list, nen co the dung vong lap for cho argv duoc (nhu ham tren). 


def myFun(arg1, *argv): 
    print('First argument: ', arg1)   # first argument 
    for arg in argv:                  # the remaining arguments are all in *argv
        print('Next argument through *argv: ', arg)

myFun('Hello', 'Welcome', 'to', 'World')
print()


# **kwargs: keyword variable, truoc khi pass gia tri phai cung cap ten cho doi so. 
# **kwargs la mot dictionary => co the lap duoc

def myFun(**kwargs): 
    for key, value in kwargs.items(): 
        print("%s = %s" % (key, value))

myFun(first = 'Geeks', mid = 'for', last = 'Geeks')
print()



# **kwargs arguments with one extra argument: 
def myFun(arg1, **kwargs): 
    for key, value in kwargs.items():
        print("%s = %s" % (key, value))

myFun('Hi', first = 'Geeks', mid = 'for', last = 'Geeks')
print()


# using *args and **kwargs to call a function: 
def myFun(arg1, arg2, arg3): 
    print('arg1: ', arg1)
    print('arg2: ', arg2)
    print('arg3: ', arg3)

args = ('Geeks', 'for', 'Geeks')
kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}

myFun(*args)
print()
myFun(**kwargs)
print()

# using *args and **kwargs in the same line to call a function: 
def myFun(*args, **kwargs): 
    print("args:", args)
    print('kwargs: ', kwargs)

myFun('geeks', 'for', 'geeks', first = 'geeks', mid = 'for', last = 'geeks')
