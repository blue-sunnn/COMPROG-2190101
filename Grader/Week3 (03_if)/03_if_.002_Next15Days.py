d, m, y = [int(e) for e in input().split()]

n = 31
d += 15

if m in [4, 6, 9, 11]: n = 30
else:
    if m == 2:
        if (y - 543) % 400 == 0:                          n = 29
        elif (y - 543) % 4 == 0 and (y - 543) % 100 != 0: n = 29
        else:                                             n = 28

if d > n:
    d -= n
    m += 1
    
if m > 12:
    m -= 12
    y += 1

print(str(d) + '/' + str(m) + '/' + str(y))
