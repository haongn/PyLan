

def swap(A, left, right, forwards = True): 
    """This function moves the element from right index to left index (by forwards)
    or moves the element from left index to right index (by backwards).
    
    left: the index of the left element to be swapped. 
    right: the index of the right element to be swapped.
    forwards: swap by forwards. 
    backwards: swap by backwards.
    A: the array contains elements."""
    if forwards == True: 
        ele = A[right]
        while right > left: 
            A[right] = A[right - 1]   # forwards element 
            right -= 1 
        A[left] = ele
    elif forwards == False: 
        ele = A[left]
        while left < right: 
            A[left] = A[left + 1]
            left += 1
        A[right] = ele 


if __name__=='__main__': 
    A = [4, 5, 2, 6, 9, 10, 1, 7]
    swap(A, 1, 5)   # swap 5 and 10 by forwards
    print(A)   
    swap(A, 2, 6, False)   
    print(A)
