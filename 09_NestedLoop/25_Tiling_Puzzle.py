def row_number(t, e):  # return row of t containing e
    for i in t:
        if e in i:
            return t.index(i)


def flatten(t):  # return a list of ints converted from list of lists of ints t
    temp = []
    for i in t:
        for j in i:
            if j != 0:
                temp.append(j)
    return temp


def inversions(x):  # return the number of inversions of list x
    c = 0
    for i in range(len(x)):
        for j in range(i, len(x)):
            if x[i] > x[j]:
                c += 1 
    return c


def solvable(t):  # return True if t is solvable
    if row_number(t, 0) % 2 == 0: nr = 0
    else: nr = 1

    if inversions(flatten(t)) % 2 == 0: ni = 0
    else: ni = 1

    if len(t) % 2 != 0 and ni == 0:
        return True
    else:
        if ni == 1 and nr == 0:
            return True
        elif ni == 0 and nr == 1:
            return True

    return False


exec(input().strip())  # this line is required for grader to work.
