x, y = [], []
xsl, ysl = [], []

c = input()

while True:
    if c == 'Zig-Zag' or c == 'Zag-Zig': break
    else:
        c = c.split()
        x += [int(c[0])]
        y += [int(c[1])]
        c = input()

for i in range(len(x)):
    if i % 2 == 0:
        xsl.append(x[i])
        ysl.append(y[i])
    else:
        xsl.append(y[i])
        ysl.append(x[i])

if c == 'Zig-Zag':
    print(min(xsl), max(ysl))
elif c == 'Zag-Zig':
    print(min(ysl), max(xsl))
