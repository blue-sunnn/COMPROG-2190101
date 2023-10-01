from math import sin, pi

dl = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

bd, bm, by, d, m, y = [int(i) for i in input().split()]

t = 0  # idk y but if I dont put this here t will keep stacking

# change from B.E. -> A.D.
by -= 543
y -= 543

# red period
t += (dl[bm - 1] - bd + 1 + sum(dl[bm:]))
#  check leap year of red period
if bm <= 2:
    if by % 400 == 0: t += 1
    elif by % 4 == 0 and by % 100 != 0: t += 1

# black period
if y - by > 0: t += 365 * (y - by - 1)

# blue period
t += (sum(dl[:m - 1]) + d - 1)
#  check leap year of blue period
if m > 1:
    if y % 400 == 0: t += 1
    elif y % 4 == 0 and y % 100 != 0: t += 1

pc = round(sin((2 * pi * t)/23), 2)
ec = round(sin((2 * pi * t)/28), 2)
ic = round(sin((2 * pi * t)/33), 2)

print("{} {:.2f} {:.2f} {:.2f}".format(t, pc, ec, ic))
