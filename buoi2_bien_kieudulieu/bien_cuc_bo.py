your_age = 10  # biến toàn cục


# function/ hàm
def pham_vi_block1():
    your_name = 'Toan Tran'  # biến cục bộ your_name

    print(your_name)
    print(your_age)  # có thể truy cập biến toàn cục bên trong hàm


pham_vi_block1()
print('Ngoài hàm')
# print(your_name) #không thể truy cập biến cục bộ bên ngoài hàm
print(your_age)  # có thể truy cập biến toàn cục bên ngoài hàm
