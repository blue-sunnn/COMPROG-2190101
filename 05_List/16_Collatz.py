n = int(input())
mtl = []

mtl.append(n)

while n != 1:
    if n % 2 == 0: n /= 2
    else: n = 3 * n + 1
    mtl.append(int(n))

if len(mtl) > 15: mtl = mtl[-15:]

for i in mtl[:-1]:
    print(str(i) + '->', end='')
print(str(mtl[-1]))
