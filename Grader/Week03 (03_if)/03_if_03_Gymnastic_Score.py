a, b, c, d = [float(i) for i in input().split()]

if a > b:
    Max1, Min1 = a, b
else:
    Max1, Min1 = b, a

if c > d:
    Max2, Min2 = c, d
else:
    Max2, Min2 = d, c

if Max1 > Max2: fMax = Max1
else:           fMax = Max2

if Min1 < Min2: fMin = Min1
else:           fMin = Min2

e = (a + b + c + d - (fMax + fMin))/2

print(round(e, 2))
