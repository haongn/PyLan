# Level: Easy
def stableSelecSort(A): 
    """See explanation below the file."""
    for i in range(len(A)): 
        curr_ind = i 
        for j in range(i + 1, len(A)): 
            if A[j] < A[curr_ind]: 
                curr_ind = j        # update the index of the min elment from i to len(A)

        # move elements from i to curr_ind forwards by 1 position
        min_ele = A[curr_ind]       # extract the min element for latter use 
        while curr_ind > i: 
            A[curr_ind] = A[curr_ind - 1]
            curr_ind -= 1 

        A[i] = min_ele              # fill the min ele from i to len(A) to position i 


if __name__=='__main__': 
    A = [4, 5, 3, 2, 4, 1]
    stableSelecSort(A)
    print(A)  



# stable ở đây có nghĩa là nếu mảng có hai phần tử bằng nhau, thì sau khi sắp xếp lại mảng, 
# thứ tự của hai phần tử đó ở mảng output phải giống với thứ tự của chúng trong mảng input. 
# (Ví dụ nếu mảng có hai phần tử A = B, A đứng trước B, thì sau khi sắp xếp, A vẫn đứng trước B). 
# Nếu ta sử dụng Selection Sort, thì lúc này sau khi sort, có khả năng A sẽ đứng sau B 
# => thứ tự ban đầu giữa A và B đã thay đổi. 

# cách sửa đổi: thay vì đổi chỗ hai phần tử trực tiếp trong Selection Sort, ta sẽ 
# chèn phần tử thấp nhất vào vị trí thích hợp trước đó, và đẩy tất cả các phần tử 
# phía sau lên 1 vị trí về phía trước (bên phải). Kỹ thuật này chính là Insertion Sort. 
