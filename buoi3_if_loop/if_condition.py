diem_trung_binh = float(input('Vui lòng nhập điểm trung bình: '))
#tổ hợp phím ctrl+/ để đóng lại những dòng đang bôi đen
# if diem_trung_binh <= 5.0: #kiểm tra điều kiện có True thì thực hiện nội dung bên dưới(trong) if
#     print('Học lực yếu')
#     print('Cần cố gắng')
#
# if diem_trung_binh >= 5.0 and diem_trung_binh < 8.0:
#     print('Học Lực Khá')
#
# if diem_trung_binh >= 8.0:
#     print('Học Lực Giỏi')

if diem_trung_binh < 5.0 and diem_trung_binh >= 0: #kiểm tra điều kiện có True thì thực hiện nội dung bên dưới(trong) if
    print('Học lực yếu & Cần cố gắng')
elif diem_trung_binh >= 5.0 and diem_trung_binh < 8.0:
    print('Học Lực Khá')
elif diem_trung_binh >= 8.0 and diem_trung_binh <= 10:
    print('Học Lực Giỏi')
else:
    print('Điểm trung bình không hợp lệ')
