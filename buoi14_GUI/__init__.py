import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox


def my_function():
    try:
        if combobox_phep_tinh.get() == 'Cộng':
            messagebox.showinfo('Kết quả',int(entry_so_thu_nhat.get()) + int(entry_so_thu_hai.get()))
        elif combobox_phep_tinh.get() == 'Trừ':
            messagebox.showinfo('Kết quả',int(entry_so_thu_nhat.get()) - int(entry_so_thu_hai.get()))
        elif combobox_phep_tinh.get() == 'Nhân':
            messagebox.showinfo('Kết quả',int(entry_so_thu_nhat.get()) * int(entry_so_thu_hai.get()))
        else:
            messagebox.showinfo('Kết quả',int(entry_so_thu_nhat.get()) / int(entry_so_thu_hai.get()))
    except:
        messagebox.showerror('Lỗi','Không thể thực hiện phép tính')

my_form = tkinter.Tk()
my_form.title('Phép Tính')
my_form.geometry('500x500')

lable_so_thu_nhat = tkinter.Label(master=my_form, text='Số thứ nhất')
lable_so_thu_nhat.grid(row=0, column=0)

entry_so_thu_nhat = tkinter.Entry(master=my_form, width=50)
entry_so_thu_nhat.grid(row=0, column=1)

lable_so_thu_hai = tkinter.Label(master=my_form, text='Số thứ hai')
lable_so_thu_hai.grid(row=1, column=0)

entry_so_thu_hai = tkinter.Entry(master=my_form, width=50)
entry_so_thu_hai.grid(row=1, column=1)

lable_phep_tinh = tkinter.Label(master=my_form, text='Phép tính')
lable_phep_tinh.grid(row=2, column=0)

combobox_phep_tinh = Combobox(master=my_form, values=('Cộng', 'Trừ', 'Nhân', 'Chia'), width=47)
combobox_phep_tinh.grid(row=2, column=1)

button_tinh = tkinter.Button(master=my_form, text='Tính', command=my_function)
button_tinh.grid(row=3, column=1)

my_form.mainloop()
