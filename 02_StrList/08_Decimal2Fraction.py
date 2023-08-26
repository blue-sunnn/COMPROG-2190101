from math import gcd

x = input().split(',')

n = int(x[0] + x[1] + x[2]) - int(x[0] + x[1])
d = (10 ** (len(x[1]) + len(x[2])) - (10 ** len(x[1])))

ans_n = n // gcd(n, d)
ans_d = d // gcd(n, d)

print(str(ans_n) + ' / ' + str(ans_d))