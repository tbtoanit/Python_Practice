class Khach_hang():
    ma_kh = ''
    ten_kh = ''
    gioi_tinh = ''
    level_kh = 0
    active = 'Yes'
    #hàm tạo init
    def __init__(self):
        pass
    #hàm nhập thông tin khách hàng
    def nhap_thong_tin_kh(self):
        self.ma_kh = input("Nhập mã kh: ")
        self.ten_kh = input("Tên kh: ")
        self.gioi_tinh = input("Nhập giới tính: ")
        self.level_kh = input("Nhập level: ")
        self.active = input("Nhập active: ")
    #hàm xuất thông tin khách hàng
    def xuat_thong_tin_kh(self):
        print(self.ma_kh, self.ten_kh, self.gioi_tinh, self.level_kh, self.active)
k1 = Khach_hang()
