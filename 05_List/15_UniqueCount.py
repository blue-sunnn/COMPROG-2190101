v = list(set(map(int, input().split())))
v.sort()
print(len(v))
if len(v) < 10:
    print(v)
else:
    print(v[:10])
