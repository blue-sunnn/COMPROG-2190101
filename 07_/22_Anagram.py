mtl1, mtl2 = [], []

n1 = input().lower().split()
n2 = input().lower().split()

for i in n1:
    mtl1 += list(i)

for i in n2:
    mtl2 += list(i)

mtl1.sort()
mtl2.sort()

if mtl1 == mtl2: print('YES')
else: print('NO')
