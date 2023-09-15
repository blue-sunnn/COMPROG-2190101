n = input().split()

n[0] = int(n[0], 2)
n[1] = int(n[1], 2)
ans = bin(n[0] + n[1])

print(ans[2:])
