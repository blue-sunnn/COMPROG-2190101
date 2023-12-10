d = list(map(int, input().split()))

p = d[-1]
i = 0
j = 0
n = len(d)

while j < n - 1:
    if d[j] <= p:
        d[i], d[j] = d[j], d[i]
        i += 1  # change here so that last line work
    j += 1

d[i], d[-1] = d[-1], d[i]

print(d)
