a = float(input())

L = U = 0
b = a

while b > 0:
    b //= 10
    U += 1

x = (L + U) / 2

while abs(a - (10 ** x)) > (10 ** -10) * max(a, 10 ** x):
    if 10 ** x > a:     U = x
    elif 10 ** x < a:   L = x
    x = (L + U) / 2

print(round(x, 6))
