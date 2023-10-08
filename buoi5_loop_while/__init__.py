# vòng lặp while
# i = 0
# while i < 15:  # điều kiện trả về True => còn lặp/loop
#     print(i)
#     i += 1  # toán tử +=
#     # i = i+1
def bt1():
    # Bài tập 1:
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    # output: [1,1,2,3,4,4]
    i = 0
    while i < len(list2):
        list1.append(list2[i])
        i += 1

    # code sắp xếp các phần tử trong listl1
    list1.sort()
    print(list1)

def bt2():
    # Bài 02: cho trước 1 chuỗi ký tự bất kỳ, hãy đếm xem trong chuỗi có bao nhiêu
    # lần xuất hiện chuỗi con là  "abc".
    s = 'tran ab abc bao abc toan'
    count_x = 0
    # output => 2
    i = 0
    while i < len(s):
    # for i in range(0, len(s)):
        if s[i] == 'a' and s[i + 1] == 'b' and s[i + 2] == 'c':
            count_x += 1

        i += 1
    print(count_x)

def bt3():
    # Bài 3: Cho trước chuỗi ký tự s, in ra chuỗi s1 là chuỗi đảo ngược các ký tự của chuỗi s.
    s = 'abc123'
    # output: '321cba'
    #print(s[0:5]) #slicing
    print(s[::-1])

def bt4(s):
    #Bài 4: Cho trước chuỗi ký tự s bất kỳ, hãy thay thế các ký tự trong chuỗi s
    # là chữ số thành ký tự $, và in ra chuỗi s mới.
    s1 = ''
    #output: '$$$abc$toan'
    for i in range(0, len(s)):
        if s[i].isdigit():
            s1 += '$'
        else:
            s1+=s[i]

    print(s1)
    #hàm kiểm tra ký tự số trong python

def bt5():
    #Bài 5:
    l1 = [2,4,3]
    for i in range(0, len(l1)):
        l1[i] = str(l1[i])

    l2 = [5,6,4]
    for j in range(0, len(l2)):
        l2[j] = str(l2[j])
    l1.reverse()
    s1 = ''.join(l1)
    l2.reverse()
    s2 = ''.join(l2)
    s = str(int(s1)+int(s2))
    s_revs = s[::-1]
    l = []
    for i in range(0, len(s_revs)):
        l.append(s_revs[i])
    print(l)

print(l1) #edited by ngandt 2023.07.10 - modify: print list l1 based on ticket #4532