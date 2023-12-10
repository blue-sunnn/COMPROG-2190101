skytrain = {}

x = input().split()
while len(x) != 1:
    k, v = x[0], x[1]
    if k not in skytrain.keys(): skytrain[k] = [v]
    else:                        skytrain[k] += [v]

    if v not in skytrain.keys(): skytrain[v] = [k]
    else:                        skytrain[v] += [k]

    x = input().split()

result = [x[0]]
if x[0] not in skytrain:
    print(x[0])
else:
    result += skytrain[result[0]]
    temp = []
    for i in result:
        temp += skytrain[i]

    for i in sorted(list(set(result + temp))): print(i)
