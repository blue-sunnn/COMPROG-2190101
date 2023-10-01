mts, mts1 = '', ''
mtl = []

while mts != 'end':
    mts = input()
    for j in mts:
        if ord('A') <= ord(j) <= ord('M') or ord('a') <= ord(j) <= ord('m'):
            mts1 += chr(ord(j) + 13)
        elif ord('N') <= ord(j) <= ord('Z') or ord('n') <= ord(j) <= ord('z'):
            mts1 += chr(ord(j) - 13)
        else:
            mts1 += j
    mtl.append(mts1)
    mts1 = ''

for i in mtl[:-1]:
    print(i)
