ca = input()
sa = input()
s = 0

if len(sa) != len(ca): print('Incomplete answer')
else:
    for i in range(len(ca)):
        if ca[i] == sa[i]: s += 1

    print(s)
