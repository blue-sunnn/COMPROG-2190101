n = int(input())
x = []
y = []

for i in range(n):
    s = list(map(int, input().split(' ')))
    x.append(s[0])
    y.append(s[1])

c = input()

xsl = []
ysl = []

for i in range(n):
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
