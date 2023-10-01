n = input().split()
s = 0

for i in n:
    s += int(i, 2)
ans = bin(s)

print(ans[2:])
