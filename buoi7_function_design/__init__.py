def sum_string(input_string):
    total = 0
    for digit in input_string: # '1221'
        total = total + int(digit)

    # for i in range(0, len(input_string)): # '1221'
    #     total = total + int(input_string[i])

    return total

#Kiểm tra cách hoạt động của function sum_string
x = sum_string('1221')
if x > 5:
    print('OK đạt')
else:
    print('Không đạt')

def hello_many_guys(*names): # intergrate
    for s in names:
        print('hello', s)

hello_many_guys('toan', 'hoa', 'hoa')
