h = int(input())
b = 2 * h - 1
j = 0

print(' ' * (h - 1) + '*' + ' ' * (h - 1))

if h > 2:
    h -= 2
    for i in range(h, 0, -1):
        j += 1
        print(' ' * i, end='')
        print('*', end='')
        print(' ' * (2 * j - 1), end='')
        print('*', end='')
        print(' ' * i, end='')
        print('')

print('*' * b)
