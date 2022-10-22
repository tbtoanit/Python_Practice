# my_string = '1-2-3-4-5-6'
# ds = my_string.split('-')
# print(ds)
import re

s = 'toan1234tran5678day987623python0886AI'
p = '[0-9]+'
ds = re.split(p, s)
print(ds)
