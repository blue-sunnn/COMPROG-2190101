plural = ['s', 'x']
vowels = ['a', 'e', 'i', 'o', 'u']

n = input()
if n[-1:] in plural or n[-2:] == 'ch':
    n = n + 'es'
elif n[-1:] == 'y':
    if n[-2:-1] in vowels: n = n + 's'
    else:                  n = n[:-1] + 'ies'
else:
    n = n + 's'

print(n)
