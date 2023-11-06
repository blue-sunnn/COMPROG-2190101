info = {}
order = []
for i in range(int(input())):
    ids, place = input().split(': ')
    order.append(ids)
    info[ids] = place.split(', ')

temp = []
n = input()
for i in info[n]:
    for k, v in info.items():
        for j in v:
            if i == j and k != n:
                temp.append(k)

if len(temp) == 0:
    print('Not Found')
else:
    for i in order:
        if i in temp: print(i)
