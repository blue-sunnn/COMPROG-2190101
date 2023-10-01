a, b, c, d = [float(i) for i in input().split()]

if a > b:
    Max1 = a
    Min1 = b
else:
    Max1 = b
    Min1 = a

if c > d:
    Max2 = c
    Min2 = d
else:
    Max2 = d
    Min2 = c

if Max1 > Max2: fMax = Max1
else: fMax = Max2

if Min1 < Min2: fMin = Min1
else: fMin = Min2

e = (a + b + c + d - (fMax + fMin))/2

print(round(e, 2))
