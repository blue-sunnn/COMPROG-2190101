fname = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nname = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']
mtl = []

n = int(input())

mtl = [(input()) for _ in range(n)]

for i in mtl:
    if i in fname: print(nname[fname.index(i)])
    elif i in nname: print(fname[nname.index(i)])
    else: print('Not found')
