ho_ten = input('Nhập thông tin tên nhân viên: ')
dia_chi = input('Nhập thông tin địa chỉ: ')
tuoi = int(input('Nhập tuổi: '))

if tuoi >= 18:
    print('Nhập thông tin nhân viên thành công')
else:
    raise Exception('Nhân viên chưa đủ tuổi lao động, buộc dừng chương trình!!!')

print('kết thúc chương trình!!!')
