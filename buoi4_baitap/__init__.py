# Cho 2 danh sách như bên dưới
# l1 = [2,5,3,8...] và l2 = [6,4,7,8,...]
# hãy in ra danh sách l3 có các phần tử là phần tử của danh sách l1 cộng với l2 theo thứ tự
# ví dụ: l3 = [8,9,... ]
l1 = [2, 5, 3, 8]
l2 = [6, 4, 7, 8]
l3 = []
for i in range(0, len(l1)):
    l3.append(l1[i] + l2[i])
print(l3)

# Bài 2:
# Cho 1 chuỗi s gồm họ và tên/fullname của 1 người, hãy trích ra chuỗi là họ của người này
# ví dụ: s = 'Nguyễn Văn An' => hãy in ra họ 'Nguyễn'
# gợi ý: dùng hàm split() chuỗi, có thể tìm hiểu thêm cách sử dụng hàm slit() trên google
s = 'Nguyễn Văn An'
thong_tin = s.split(' ')
print(thong_tin[0])

# Bài 3:
# Cho 1 số a, hãy in ra True nếu số a chỉ chia hết cho 1 và chính a (không chia hết cho bất cứ
# số nào khác), ví dụ: a = 7 => in ra True, vì 7 chỉ chia hết cho 1 và 7
# gợi ý: hãy xét những số i từ 2,3,4...,6, nếu a%i == 0 thì xem như False
# kiểm tra nếu a là số nguyên tố thì in True, only/ chỉ chia hết cho 1 và chính nó
a = int(input('nhập sn:'))
for i in range(2, a):
    if a % i == 0:  # if n chia hết cho i phần tử thì đổi mặc định lại then in ra, không cần else nào khác vì mặc định ban đầu là True
        print(False)
        break
else:  # else của for
    print(True)  # Nếu không break thì else này sẽ được thực thi

# Bài 4: hãy in ra vị trí của nguyên âm trong chuỗi s = 'mot chuoi nao do',
# biết rằng nguyên âm sẽ bao gồm các ký tự: u e o a i
# Ví dụ: s = 'abcd123' => vị trí được in ra là 0
# Ví dụ: s = '0123abiw' => vị trí được in ra là 4, 6
s1 = '0123abiw'
for i in range(0, len(s1)):
    if s1[i] in ('u', 'e', 'o', 'a', 'i'):
        print(i)

