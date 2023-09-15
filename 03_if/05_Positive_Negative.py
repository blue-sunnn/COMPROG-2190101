n = input()

if n[0] == '-':
    print('negative')
elif n[0] == '0':
    print('zero')
else:
    print('positive')

if int(n) % 2 == 0:
    print('even')
else:
    print('odd')
