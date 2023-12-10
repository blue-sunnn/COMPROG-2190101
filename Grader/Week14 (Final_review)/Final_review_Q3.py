import numpy as np

def f1(a):
    # !!! YOUR CODE HERE !!!
    n = int(a.shape[0] / 3)
    m = int(a.shape[1] / 3)
    return a[n:2 * n, :m] - a[n:2 * n, 2 * m:]


# main
a = np.array([int(x) for x in input().split()])
r, c = [int(x) for x in input().split()]
a = a.reshape(r, c)
print(f1(a))
