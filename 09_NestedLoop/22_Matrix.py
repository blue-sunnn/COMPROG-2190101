def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m


def mult_c(c, A):
    m = []
    for i in A:
        r = []
        for j in i:
            j *= c
            r.append(j)
        m.append(r)
    return m


def mult(A, B):
    m = []
    for Ai in A:
        t = []
        for x in range(len(B[0])):
            Bj = [i[x] for i in B]
            Ci = sum([Ai[y]*Bj[y] for y in range(len(Ai))])
            t.append(Ci)
        m.append(t)
    return m


exec(input().strip())  # this line is required for grader to work.
