def first_fit(L, e):  # put e into sublist inside L by first fit
    for i in L:
        if sum(i) + e <= 100:
            i.append(e)
            return
    L.append([e])


def best_fit(L, e):  # put e into sublist inside L by best fit
    q = []
    for i in L:
        if 100 - sum(i) - e >= 0: q.append(100 - sum(i) - e)
        else:                     q.append(100)

    if len(q) == 0:  L.append([e])
    else:
        m = min(q)
        if m == 100: L.append([e])
        else:        L[q.index(m)].append(e)


def partition_FF(D):  # return a list of the partitioned data from D using first fit
    L = []
    for i in D: first_fit(L, i)
    return L


def partition_BF(D):  # return a list of the partitioned data from D using best fit
    L = [[D[0]]]
    for i in D[1:]: best_fit(L, i)
    return L


exec(input().strip())  # this line is required for grader to work.
