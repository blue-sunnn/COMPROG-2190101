mtl, mtl1 = [], []

# First set
a = int(input())
mtl = [(int(input())) for _ in range(a)]

# Second set
mtl += list(map(int, input().split()))

# Third set
b = 0
while b != -1:
    b = int(input())
    mtl.append(b)

mtl = mtl[:-1]  # not include '-1' in list
for i in range(len(mtl)):
    if i % 2 == 0: mtl1.append(mtl[i])
    else: mtl1.insert(0, mtl[i])

print(mtl1)
