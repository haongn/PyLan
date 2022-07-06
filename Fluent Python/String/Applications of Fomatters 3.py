# Given a list of float values, the task is to truncate all float values to 2-decimal digits. 

input = [100.7689454, 17.232999, 60.98867, 300.83748789]

output = ['{:.2f}'.format(ele) for ele in input]  # listcomp + formatting

print(output)

# Nhan xet: Nhuoc diem o day la list output gom cac phan tu la string, khong phai la cac so. 

# de output co cac phan tu la cac so: 
output = [float('{:.2f}'.format(ele)) for ele in input]

print(output)

# problem solved!













