import string

symbols = string.punctuation
mts = ''
mtl1 = []
n = list(input())

for i in range(len(n)):
    if n[i] not in symbols: 
        mts += n[i]
    else: 
        mts += ' '

mtl = mts.lower().split()
print(mtl[0], end='')
for i in mtl[1:]:
    print(i.title(), end='')
