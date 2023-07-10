# Viết hàm nhận vào 1 danh sách, in ra số là tổng các phần tử trong danh sách
def sum_list(l):
    tong = 0
    for i in range(0, len(l)):
        tong = tong + l[i]
    print(tong)


sum_list([1, 2, 3, 6, 9])  # => 6
print('test commit, push git!,')# nguyenhoai test git