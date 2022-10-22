'''
Hãy kết nối tới CSDL đã tạo sẵn, tạo ra một table dữ liệu khách hàng để quản lý các thông tin như: Mã KH, tên KH, điểm tích lũy, địa chỉ khách hàng.
a/ Viết một function cho người dùng input từ màn hình console/terminal thông tin khách hàng và insert vào trong database
b/ Một function cho phép cập nhật thông tin khách hàng trong table, thông tin dữ liệu cập nhật là tùy ý người dùng và thông tin khách hàng cần cập nhật cần được xác minh bởi người sử dụng qua mã khách hàng. tất cả dữ liệu được input qua màn hình console.
c/Một function cho phép xóa một hoặc nhiều khách hàng thông qua mã khách hàng, nếu nhiều khách hàng, người dùng có thể input từ màn hình console dưới dạng ví dụ: KH001,KH002,KH003,...
d/Viết một function để cho phép người dùng tìm kiếm thông tin chi tiết một khách hàng qua mã khách hàng được input từ ngoài màn hình console.
'''

import pyodbc

server = 'DLAP-0063'
database = 'QUAN_LY_KHACH_HANG'
conn = pyodbc.connect(
'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
cursor = conn.cursor()

print('Connected!')

def tao_khach_hang():
    ma = input('Nhập mã: ')
    ten = input('Nhập tên: ')
    diem = input('Nhập điểm: ')
    dc = input('Địa chỉ: ')
    tao_moi = "INSERT INTO KHACH_HANG(MA_KH, TEN_KH, DIEM_THUONG, ADDRESS_KH) VALUES('{0}',N'{1}','{2}',N'{3}')".format(ma, ten, diem, dc)
    cursor.execute(tao_moi)
    cursor.commit()
    print('Thêm mới thành công!')

def cap_nhat_kh():
    ma = input('Bạn muốn cập nhật thông tin cho khách hàng có mã là? ')
    option = input('''
    Bạn muốn cập nhật thông tin gì của khách hàng trên?
    Nhập 1 để cập nhật tên
    Nhập 2 để cập nhật điểm
    Nhập 3 để cập nhật địa chỉ
    ''')

    if option == '1':
        cap_nhat = "UPDATE KHACH_HANG SET TEN_KH = N'{0}' WHERE MA_KH = '{1}'".format(input('Bạn Muốn cập nhật thành tên gì?'),ma)
    elif option == '2':
        cap_nhat = "UPDATE KHACH_HANG SET DIEM_THUONG = '{0}' WHERE MA_KH = '{1}'".format(input('Bạn Muốn cập nhật thành bao nhiêu?'),ma)
    else:
        cap_nhat = "UPDATE KHACH_HANG SET ADDRESS_KH = N'{0}' WHERE MA_KH = '{1}'".format(input('Bạn Muốn cập nhật thành dc nào?'),ma)

    cursor.execute(cap_nhat)
    cursor.commit()

def xoa_kh():
    kh = input('Vui lòng nhập những khách hàng cần xóa: ') #'kh01,kh02,kh03'
    ds_kh = kh.split(',') #ds_kh = ['KH01','KH02','KH03']
    for ma in ds_kh:
        cursor.execute(" DELETE FROM KHACH_HANG WHERE MA_KH = '{0}' ".format(ma))
        cursor.commit()

def tim_kiem_theo_ten():
    option = input('''
    Bạn muốn tìm kiếm thông tin khách hàng theo option nào bên dưới?
    1. theo tên
    2. theo mã
    3. theo địa chỉ
    ''')
    if option == '1':
        tim_kiem = "SELECT * FROM KHACH_HANG WHERE TEN_KH LIKE '%{0}%'".format(input('Nhập tên khách hàng muốn tìm: '))
    elif option == '2':
        tim_kiem = "SELECT * FROM KHACH_HANG WHERE MA_KH = '{0}'".format(input('Nhập mã khách hàng muốn tìm: '))
    else:
        tim_kiem = "SELECT * FROM KHACH_HANG WHERE ADDRESS_KH LIKE '%{0}%'".format(input('Nhập dc khách hàng muốn tìm: '))
    result = cursor.execute(tim_kiem)
    data = result.fetchall()

    print(data)

tim_kiem_theo_ten()
