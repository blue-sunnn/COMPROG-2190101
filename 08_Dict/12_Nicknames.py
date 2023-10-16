def reverse(d):
    temp = {d[k]: k for k in d}
    return temp


nameDic = {}
nameList = []

for i in range(int(input())):
    real, nick = input().split()
    nameDic[real] = nick

for i in range(int(input())):
    nameList.append(input())

rnameDic = reverse(nameDic)

for i in nameList:
    if i in nameDic.keys():
        print(nameDic[i])
    elif i in rnameDic.keys():
        print(rnameDic[i])
    else:
        print('Not found')
