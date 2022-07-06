# Level: Easy 

def optimized_bubble_sort(A): 
    """This is an optimized implementation of Bubble Sort algorithm."""
    n = len(A)
    for i in range(n): 
        swapped = False 
        for j in range(0, n - i - 1): 
            if A[j] > A[j + 1]: 
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True

        if swapped == False: 
            print('Stop early!')
            break 


if __name__=='__main__': 
    A = [64, 34, 25, 12, 22, 11, 90]
    optimized_bubble_sort(A)
    print(A)

# Ta có thể tối ưu hóa hàm Bubble Sort, khi nhận thấy rằng, trong một vòng pass, 
# nếu không có hai phần tử nào được đổi chỗ cho nhau, suy ra khi đó các phần tử đã được 
# sắp xếp theo đúng thứ tự (vì khi so sánh hai phần tử kề nhau, phần tử phía sau 
# luôn nhỏ hơn phần tử phía trước, và khi tiến lên 1 vị trí thì phần tử phía sau lại 
# vẫn nhỏ hơn phần tử phía trước, cứ thế...)

# Cách làm: Nếu có một vòng pass mà không có sự đổi chỗ nào thì ta đặt thêm một biến swap = False
# rồi sau đó dừng vòng lặp. 