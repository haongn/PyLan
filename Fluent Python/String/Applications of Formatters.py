# Formatters are generally used to Organize Data. 
# Formatters can be seen in their best light when they are being used to organize a lot of data 
# in a visual way. 
# If we are showing databases to users, using formatters to increase field size 
# and modify alignment can make the output more readable.


# ex: orginize large data using format()
def unorganized(a, b):   
    """This function print result in a normal way, which is unorganized."""
    for i in range(a, b):
        print(i, i**2, i**3, i**4)

def organized(a, b): 
    """This funtion print values in an organized manner."""
    for i in range(a, b): 
        print('{:6d}{:6d}{:6d}{:6d}'.format(i, i**2, i**3, i**4))  # number are right aligned (by default)


if __name__ == '__main__':
    unorganized(3, 10)
    organized(3, 10)


    










