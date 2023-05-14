import re

my_pattern = '[0-9]{10}'
data_input = input('Vui lòng nhập số điện thoại: ')

result = re.fullmatch(my_pattern, data_input)
if result != None:
    print('Số điện thoại bạn nhập đúng định dạng gồm 10 chữ số')
else:
    print('Số điện thoại nhập sai định dạng')

'abc@.com'
# testing for GitHub