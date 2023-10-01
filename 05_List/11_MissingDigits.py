s = input()
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
mtl, mtl1 = [], []

mtl = [i for i in s if (i in num) and (i not in mtl)]
mtl.sort()
mtl1 = [i for i in num if (i not in mtl)]

if len(mtl1) > 0: print(','.join(mtl1))
else: print('None')
