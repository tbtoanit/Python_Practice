def print_many_hello():
    # nhóm các lệnh
    for i in range(0, 10):
        print('Hello')


# from buoi5_loop_while import bt5
# bt5()

def cong_hai_so(a,b):  # argument
    print(a + b)


def phep_tinh(x, y, z):
    if z == '+':
        print(x + y)
    if z == '-':
        print(x - y)
    if z == '*':
        print(x * y)
    if z == '/':
        print(x / y)


def kiem_tra_so(x):
    if x % 2 == 0:
        print('chẵn')
    else:
        print('lẻ')

print_many_hello()
