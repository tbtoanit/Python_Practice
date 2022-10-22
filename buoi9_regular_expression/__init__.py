import re

p = '[a-z0-9_]+[@][a-z0-9]+.com'
my_string = input('Vui lòng nhập vào email cần kiểm tra: ')

# remark = re.fullmatch(p, my_string)
# remark = re.match(p,my_string)
remark = re.findall(p,my_string)
print(remark)
if remark != None:
    print('Email chính xác')
else:
    print('Email không chính xác')
