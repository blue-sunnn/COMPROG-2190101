il = input()
mtl = [0] * len(il)

for i in range(len(il)):
    if il[i] == '(':
        mtl[i] = '['
    elif il[i] == '[':
        mtl[i] = '('
    elif il[i] == ')':
        mtl[i] = ']'
    elif il[i] == ']':
        mtl[i] = ')'
    else:
        mtl[i] = il[i]

mtl = ''.join(mtl)

if mtl == il: print(il)
else: print(mtl)
