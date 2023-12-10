n = input().split()

fname, acyr = n[0], n[1][-2:]
mtl = []

f = open(fname, 'r')
for line in f:
    x = line.split()
    if x[0][:2] == acyr:
        mtl.append(float(x[1]))
f.close()

if len(mtl) == 0:
    print('No data')
else:
    print(min(mtl), max(mtl), sum(mtl) / len(mtl))
