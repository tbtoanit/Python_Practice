# Bài 1: copy toàn bộ nội dung của file input_file.txt vào trong input_file2.txt
# open file 1, read noi dung file 1 => biến a
# open file 2, write vào file 2 => biến a
f = open('input_file.txt', encoding='UTF_8', mode='r')
data = f.read()
newfile = open('input_file2.txt', encoding='UTF_8', mode='r+')

newfile.write(data)
p = newfile.read()
print(p)
# Bài 2: Đọc nội dung file sau đây và tiến hành in ra những số hợp đồng trong file
# Biết rằng số hợp đồng sẽ có định dạng: 1 ký tự chữ cái in hoa đầu tiên và 7 ký tự số liền
# kề sau đó. Ví dụ: A1234567
import re

p = '[A-Z][0-9]{7}'
f = open('data.txt')
my_string = f.read()
print(my_string)
ds = re.findall(p, my_string)
print(ds)
