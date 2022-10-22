# Viết hàm nhận vào 1 danh sách, và in ra những phần tử trong danh sách đó là số lẻ
def in_so_le(l):
    for i in range(0, len(l)):
        if l[i]%2 != 0:
            print(l[i])

in_so_le([1, 3, 5, 6, 8, 0])
