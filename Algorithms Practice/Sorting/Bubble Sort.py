# Level: Easy. The simplest sorting algorithm. 

def bubble_sort(A): 
    """This is the simplest sorting algorithm."""
    n = len(A)
    for i in range(n): 
        # Last i elements are already in place 
        for j in range(0, n - i - 1):  # loop to n - i - 2
            if A[j] > A[j + 1]: 
                A[j], A[j + 1] = A[j + 1], A[j]


if __name__=='__main__': 
    A = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(A)
    print(A)


# Nhận xét: TT này sẽ sắp xếp từ bên phải trước. Tại mỗi vòng, nó sẽ đẩy được phần tử 
# lớn nhất về phía bên phải. 