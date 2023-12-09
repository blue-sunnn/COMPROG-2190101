h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

# change hr & min -> s
t1 = (h1 * 3600) + (m1 * 60) + s1
t2 = (h2 * 3600) + (m2 * 60) + s2

# calculate the diff between t1 & t2
# using + and % to get positive value
dt = t2 - t1

dh = (24 + (dt // 3600)) % 24
dt -= dh * 3600

dm = (60 + (dt // 60)) % 60
dt -= dm * 60

ds = (60 + dt) % 60

print(str(dh) + ":" + str(dm) + ":" + str(ds))
