temp = []

for i in range(int(input())):
    c = 0
    x = input()
    for j in x:
        if j == '.': c += 1
        else: break
    temp.append('.' * (c // 2) + x[c:])

for i in temp:
    print(i)
