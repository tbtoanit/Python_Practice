# Bai1: Hãy viết hàm nhận vào 1 danh sách gồm 5 số tự nhiên, và thực hiện tính
# tổng của 5 tham số đó.
# trong trường hợp người dùng đưa vào tham số là 1 danh sách nhiều hơn 5 số tự nhiên,
# thì chương trình buộc dừng lại
def add_numbers(l):
    if len(l) > 5:
        raise Exception('Danh sách nhiều hơn 5 giá trị, buộc dừng chương trình')

    tong = 0
    for i in l:
        tong += i
    return tong


x = add_numbers([1, 4, 3, 2, 6, 8])
print(x)
