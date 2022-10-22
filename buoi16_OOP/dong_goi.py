class Person():
    name = ""
    age = 0
    __address = "" #write only qua hàm set_address()
    __password = "abcd123!" #muốn cài đặt password là read only, đọc qua get_password()
    def __init__(self):
        pass
    def insert(self):
        print("Insert New One")
    def get_password(self):
        print(self.__password)

    def set_address(self, a):
        self.__address = a
p1 = Person()
p1.name = "Person 1"
p1.get_password()
p1.set_address("hcm")
