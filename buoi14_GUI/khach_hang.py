from tkinter import messagebox

import pyodbc

server = 'DLAP-0063'
database = 'QUAN_LY_KHACH_HANG'
conn = pyodbc.connect(
'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
cursor = conn.cursor()

print('Connected!')

def tao_khach_hang():
    ma = entry_ma_khach_hang.get()
    ten = entry_ten_khach_hang.get()
    diem = ''
    dc = entry_dia_chi.get()
    tao_moi = "INSERT INTO KHACH_HANG(MA_KH, TEN_KH, DIEM_THUONG, ADDRESS_KH) VALUES('{0}',N'{1}','{2}',N'{3}')".format(ma, ten, diem, dc)
    cursor.execute(tao_moi)
    cursor.commit()
    messagebox.showinfo('Thông Báo','Thêm mới thành công!')

import tkinter

my_form=tkinter.Tk()
my_form.title('Khách Hàng')
my_form.geometry("500x500")

lable_ma_khach_hang=tkinter.Label(master=my_form,text='Mã Khách Hàng') #datatype: Label
lable_ma_khach_hang.grid(row=0,column=0)
entry_ma_khach_hang=tkinter.Entry(master=my_form,width=50)
entry_ma_khach_hang.grid(row=0,column=1)

lable_ten_khach_hang=tkinter.Label(master=my_form,text='Tên Khách Hàng')
lable_ten_khach_hang.grid(row=1,column=0, pady=10)
entry_ten_khach_hang=tkinter.Entry(master=my_form,width=50)
entry_ten_khach_hang.grid(row=1,column=1, pady=10)

lable_dia_chi=tkinter.Label(master=my_form,text='Địa Chỉ')
lable_dia_chi.grid(row=2,column=0)
entry_dia_chi=tkinter.Entry(master=my_form,width=50)
entry_dia_chi.grid(row=2,column=1)


button_tao_moi=tkinter.Button(master=my_form,text='Thêm mới khách hàng',command=tao_khach_hang)
button_tao_moi.grid(row=3,column=1, pady=10)
my_form.mainloop()


