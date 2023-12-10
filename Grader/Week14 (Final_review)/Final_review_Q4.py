import numpy as np

def f2(a):
    # !!! YOUR CODE HERE !!!
    w = a[::2, 1::2]
    r = w.reshape([1, -1])
    return r


# main
a = np.array([x for x in input().split()])
r, c = [int(x) for x in input().split()]
a = a.reshape(r, c)
print(f2(a))
