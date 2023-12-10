import math

X, M, S = input().split()
x, m, s = float(X), float(M), float(S)

if x > 0 and m != 0 and s > 1:
    print(round(((2 * math.pi) ** (-0.5)) * (s ** (-1)) * (math.e ** (-0.5 * (((x - m)/s) ** 2))), 2))
else:
    print('Invalid input')
