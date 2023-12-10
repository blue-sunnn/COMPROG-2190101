def add_poly(p1, p2):
    temp = {}
    if p1 != []:
        for i, j in p1:
            if j not in temp: temp[j] = i
            else:             temp[j] += i

    if p2 != []:
        for i, j in p2:
            if j not in temp: temp[j] = i
            else:             temp[j] += i

    temp1 = sorted([(-v, k) for v, k in temp.items() if k != 0])
    return [(j, -i) for i, j in temp1]


def mult_poly(p1, p2):
    temp = {}
    for i1, j1 in p1:
        for i2, j2 in p2:
            j = j1 + j2
            i = i1 * i2
            if j not in temp: temp[j] = i
            else:             temp[j] += i

    temp1 = sorted([(-v, k) for v, k in temp.items() if k != 0])
    return [(j, -i) for i, j in temp1]


# You must have 2 lines below to submit to grader
for i in range(3):
    exec(input().strip())
