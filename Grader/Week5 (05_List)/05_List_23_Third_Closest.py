mtl = []

for i in range(int(input())):
    x = input().split()
    d = (float(x[0]) ** 2 + float(x[1]) ** 2) ** 0.5 
    mtl.append([d, i + 1, x[0], x[1]]) 

mtl.sort() 
z = mtl[2] 
print('#' + str(z[1]) + ': ' + '(' + str(round(float(z[2]), 2)) + ', ' + str(round(float(z[3]), 2)) + ')')
