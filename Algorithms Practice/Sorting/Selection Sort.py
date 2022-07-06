# Level: Easy 

def selection_sort(A): 
    """See explanation below of the file.
    
    Note: This is a sequential sorting algorithm."""
    for i in range(len(A)): 
        curr_ind = i                     # current index of the sorted element
        # find the index of the min element from i to len(A)
        for j in range(i + 1, len(A)):   # j: biến chạy 
            if A[j] < A[curr_ind]:     # curr_ind: biến chỉ index của min ele từ i đến len(A)
                curr_ind = j             

        # swap the found min element with the current ith index element 
        A[i], A[curr_ind] = A[curr_ind], A[i]


if __name__=='__main__': 
    A = [64, 25, 12, 22, 11]
    B = [34, 27, 6, 1, 4, 9, 25, 12, 8]
    selection_sort(A)
    selection_sort(B)
    print(A)
    print(B)

            
# Level: Easy 
# The selection sort algorithm sorts an array by repeatedly finding the minimum element 
# (considering ascending order) from unsorted part and putting it at the beginning. 

# The algorithm maintains two subarrays in a given array.
# 1) The subarray which is already sorted. 
# 2) Remaining subarray which is unsorted.
# In every iteration of selection sort, the minimum element (considering ascending order) from 
# the unsorted subarray is picked and moved to the sorted subarray.