import string

mts = ''
n = list(input())

for i in range(len(n)):
    if n[i] not in string.punctuation: 
        mts += n[i]
    else: 
        mts += ' '

mtl = mts.lower().split()

print(mtl[0], end='')

for i in mtl[1:]:
    print(i.title(), end='')
