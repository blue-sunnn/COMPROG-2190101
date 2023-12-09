mtl, mtl1 = [], []
data1, data2 = input().split()

f1, f2 = open(data1, 'r'), open(data2, 'r')

for i in f1:
    a, b = i.split()
    mtl.append([a[-2:], a[:-2], b])
f1.close()

for i in f2:
    a, b = i.split()
    mtl.append([a[-2:], a[:-2], b])
f2.close()

for i in sorted(mtl):
    mtl1.append(i[1] + i[0] + ' ' + i[2])

for i in mtl1: print(i)
