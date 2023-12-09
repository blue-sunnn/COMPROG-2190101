mtl1, mtl2 = [], []

for i in input().lower().split():
    mtl1 += list(i)

for j in input().lower().split():
    mtl2 += list(j)

if sorted(mtl1) == sorted(mtl2): print('YES')
else:                            print('NO')
