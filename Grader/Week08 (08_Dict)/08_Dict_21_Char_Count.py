import string

s = [i for i in list(input().lower()) if i in string.ascii_lowercase]

dic = {}
for c in s:
    dic[c] = s.count(c)

for i in sorted([[-y, x] for x, y in dic.items()]):
    print(str(i[1]) + ' -> ' + str(-i[0]))
