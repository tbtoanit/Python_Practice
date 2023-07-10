# In ra những số chia hết cho 3 trong khoảng từ 1=>30 (bao gồm cả 30)
# gợi ý:
for i in range(1, 31, 1):
    if i % 3 == 0:
        print(i)

for j in range (1,50,1):
    if j % 2 == 0:
        print (j)

# Tính tổng các giá trị từ 1 => n, với n là số do người dùng nhập vào input()
# ví dụ n = 5 thì tổng = 1+2+...+5
# Gợi ý: sử dụng toán tử +=
n = int(input('Nhập vào n: '))
tong = 0
for i in range(1, n + 1):
    tong += i

print(tong)

# https://leetcode.com/problems/two-sum/
nums = [2, 8, 11, 15, 7]
target = 9

for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j]) #edit by toan tran 2023.07.10 - print list instead of variable #3412

#i=0: 2+8, 2+11, 2+15, 2+7. j =1,2,3,4
#i=1: 8+11, 8+15, 8+7. j=2,3,4
#i=2: j=3,4
