n = int(input())

if n // (10 ** 9) > 0:
    n = n / (10 ** 9)
    alp = 'B'
elif n // (10 ** 6) > 0:
    n = n / (10 ** 6)
    alp = 'M'
elif n // (10 ** 3) > 0:
    n = n / (10 ** 3)
    alp = 'K'
else:
    alp = ''

if n > 9:   print(str(round(n)) + alp)
else:       print(str(round(n, 1)) + alp)
