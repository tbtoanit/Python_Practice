try:
    print(int(input('nhập vào số bị chia: '))/int(input('nhập vào số chia: ')))
except:
    pass
else:
    print('Không bị exception')
finally:
    print('Đoạn code luôn luôn được chạy')

print('Kết thúc chương trình')
