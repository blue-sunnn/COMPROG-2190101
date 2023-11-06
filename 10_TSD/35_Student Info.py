info = {}
temp = []
for i in range(int(input())):
    name, group, gen, department = input().split()
    info[name] = [group, gen, department]

x = set(input().split(' '))
for k, v in info.items():
    if x.issubset(v):
        temp.append([k, v])

if len(temp) == 0:
    print('Not Found')
else:
    for i, j in sorted(temp):
        print(i, j[0], j[1], j[2])
