from math import sqrt

try:
    x = sqrt(int(input('Nhập vào số cần tính căn bậc 2: ')))
    print(x)
except:
    print('Căn bậc 2 không thể tính cho số âm')

try:
    l = [0, 1, 2, 3, 4, 5]
    print(l[9])
except:
    print('Bạn đang truy xuất phần tử ngoài danh sách')
