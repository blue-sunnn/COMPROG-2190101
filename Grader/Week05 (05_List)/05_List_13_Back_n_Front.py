mtl, mtl1 = [], []

# First set
mtl = [(int(input())) for _ in range(int(input()))]

# Second set
mtl += list(map(int, input().split()))

# Third set
b = 0
while b != -1:
    b = int(input())
    mtl.append(b)

mtl = mtl[:-1]
for i in range(len(mtl)):
    if i % 2 == 0:  mtl1.append(mtl[i])
    else:           mtl1.insert(0, mtl[i])

print(mtl1)
