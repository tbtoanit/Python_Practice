# Khai báo biến có kiểu dữ liệu là kiểu str/string
my_name = 'Tran Bao Toan'
my_age = "30"
print(my_name + my_age)

truyen_kieu = "Dòng thứ nhất" \
              "dòng thứ hai" \
              "dòng thứ 3" \
              "....."
truyen_kieu_1 = """
                Dòng thứ nhất
                Dòng thứ hai
                Dòng thứ 3
                """

# Kiểu dữ liệu number
so_nguyen_1 = 10  # kiểu dữ liệu int / integer
so_thap_phan = 10.5  # kiểu dữ liệu float, số thực
so_phuc_1 = 10 + 2j  # kiểu dữ liệu số phức, complex

# kiểu dữ liệu tập hợp, tích hợp, collection, intergrate
# danh sách, list
thong_tin_hoc_vien_1 = ['Toan Tran', 30, 'Python', '10,000,000', 'Python']
print(thong_tin_hoc_vien_1[2])
thong_tin_hoc_vien_1[1] = 40
print(thong_tin_hoc_vien_1)
thong_tin_hoc_vien_1.append('Final Element')
print(thong_tin_hoc_vien_1)

# Mapping/ Dictionary truy xuất value thông qua key
danh_sach_hoc_vien = {'001': 'Toan Tran', '002': 'The Anh', '003': 'Van An'}
print(danh_sach_hoc_vien.get('002'))

# Set, tập hợp
danh_sach_mon_hoc = {'Python', 'Java', '.Net', 'PHP', 'Oracle Database', 'Python'}
print(danh_sach_mon_hoc)
print('Java' in danh_sach_mon_hoc)
print('Python' not in danh_sach_mon_hoc)

#tuple: read only, không cho thay đổi, cập nhật dữ liệu của biến kiểu tuple
thong_tin_hoc_vien_2 = ('Toan Tran', 30, 'Python', '10,000,000', 'Python')
print(thong_tin_hoc_vien_2[1])
#thong_tin_hoc_vien_2[1] = 40 #lỗi, không thể cập nhật giá trị của phần tử số 1

#Boolean có 2 giá trị True Flase
t = True #khai báo kiến t kiểu boolean có giá trị là True
f = False

#bytes
address = b'10xb13'
