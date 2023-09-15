n = int(input())
mtl = []

for i in range(n):
    x = input().split()
    d = (float(x[0]) ** 2 + float(x[1]) ** 2) ** 0.5  # calculate distance
    y = []
    # use extend to append multiple element in list
    y.extend([d, i + 1, x[0], x[1]])
    mtl.append(y)  # append list in mtl

mtl.sort()  # sort by distance
z = mtl[2]  # get the third element
print('#' + str(z[1]) + ': ' + '(' + str(round(float(z[2]), 2)) + ', ' + str(round(float(z[3]), 2)) + ')')
