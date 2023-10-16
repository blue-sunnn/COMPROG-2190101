import string

s = [i for i in list(input().lower()) if i in string.ascii_lowercase]

dic = {}
for i in s:
    x = s.count(i)
    dic[i] = x

temp = sorted([[-y, x] for x, y in dic.items()])

for i in temp:
    print(str(i[1]) + ' -> ' + str(-i[0]))
