q = ''
s = i = 0

while q != 'q':
    q = input()
    if q == 'q':
        break
    else:
        s += float(q)
        i += 1

if i > 0:
    print(round(s / i, 2))
else:
    print('No Data')
