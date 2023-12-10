def factor(N):  # N is positive integer greater than 1
    k = 2
    temp = []
    while True:
        if N % k == 0:
            N /= k
            temp.append(k)
        else:
            k += 1
        if N == 1: break

    d = {}
    for i in temp:
        if i not in d.keys(): d[i] = 1
        else:                 d[i] += 1
    return sorted([[k, v] for k, v in d.items()])


exec(input().strip())  # this line is required for grader to work.
