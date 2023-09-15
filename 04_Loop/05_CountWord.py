k = input()
s = input()
count = 0
symbols = ['(', ')', "'", '.', '"', ',']
mtl = []

for i in s:
    if i not in symbols:
        mtl.append(i)
    else:
        mtl.append(' ')

s = ''.join(mtl)

for i in s.split():
    if i == k:
        count += 1

print(count)
