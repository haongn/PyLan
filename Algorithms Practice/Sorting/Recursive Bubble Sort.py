# Level: Easy 

def recur_bubble_sort(A, n): 
    """This is a recursive (and optimized) version of Bubble Sort algorithm."""
    # Degenerate case: 
    if n == 1: 
        return 
    
    # Recursive part: 
    swapped = False
    for j in range(0, n - 1): 
        if A[j] > A[j + 1]: 
            A[j], A[j + 1] = A[j + 1], A[j]
            swapped = True 
        
    if swapped == False: 
        print('Stop early!')
        return 
    
    recur_bubble_sort(A, n - 1)


if __name__=='__main__': 
    A = [64, 34, 25, 12, 22, 11, 90]
    recur_bubble_sort(A, len(A))
    print(A)
    B = [2, 7, 3, 19, 6, 34, 10, 8, 20, 16, 25, 23]
    recur_bubble_sort(B, len(B))
    print(B)



# Nhận xét: Ta có thể dễ dàng hình dung ra được công thức truy hồi, vì 
# về cơ bản, các hàm truy hồi thực hiện theo thứ tự lần lượt chứ không thực hiện 
# lồng vào nhau. Vì vậy, hàm chỉ cần hai tham số là mảng A và n: chỉ số index cuối cùng 
# cần lặp đến của vòng pass tiếp theo.