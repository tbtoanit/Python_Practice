#Design kiểu dữ liệu Employee
class Employee(): #class
    #Properties/ thuộc tính
    employee_name = ""
    employee_age = 18

    #Hàm tạo init/ constructor
    def __init__(self): # initialize: khởi tạo
        print("Bạn đang gọi đến 1 hàm tạo")

    #function/ hàm
    def get_employee_info(self):
        print(self.employee_name)


#ứng dụng kiểu dữ liệu class Employee tạo ra biến/đối tượng
e = Employee() #object e: dataype: Employee
#gán thông tin cho đối tượng e
e.employee_name = "Nguyen Van Anh"
e.employee_age = 22
e.get_employee_info()


# e1 = Employee()
# e1.employee_name = "Trần Thị Chị"
# e1.employee_age = 19
