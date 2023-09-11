d = list(map(int, input().split()))
c = 0

for i in range(1, len(d) - 1) :
  if d[i - 1] < d[i] > d[i + 1] : c += 1

print(c)