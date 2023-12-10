def reverse(d):
    temp = {d[k]: k for k in d}
    return temp


YellowPage = {}

for i in range(int(input())):
    x = input().split()
    name, tel = x[0] + ' ' + x[1], x[-1]
    YellowPage[name] = tel

rYellowPage = reverse(YellowPage)

for i in [input() for _ in range(int(input()))]:
    if i in YellowPage:     print(i + ' --> ' + YellowPage[i])
    elif i in rYellowPage:  print(i + ' --> ' + rYellowPage[i])
    else:                   print(i + ' --> ' + 'Not found')
