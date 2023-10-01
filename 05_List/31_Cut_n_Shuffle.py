d = input().split()
o = input()
n = int(len(d) / 2)

for i in range(len(o)):
    if o[i] == 'C':
        d = d[n:] + d[:n]
    elif o[i] == 'S':
        temp = []
        for j in range(n):
            temp.append(d[j])
            temp.append(d[j + n])
        d = temp
print(' '.join(d))
