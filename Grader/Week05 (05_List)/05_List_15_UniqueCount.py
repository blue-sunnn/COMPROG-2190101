v = sorted(set(map(int, input().split())))

print(len(v))

if len(v) < 10: print(v)
else:           print(v[:10])
