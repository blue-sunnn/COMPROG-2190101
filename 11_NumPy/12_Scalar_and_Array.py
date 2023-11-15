import numpy as np

def toCelsius(f):
    # f = [temperature in Fahrenheit, …]
    return (f - 32) / (1.8)


def BMI(wh):
    # [[w1,h1],[w2,h2], …]
    bmi = wh[::, :1:] / ((wh[::, 1::] * 0.01) ** 2)
    return bmi.T[0]


def distanceTo(p, P):
    # distance from p to all points in P
    X = P[:, 0]
    Y = P[:, 1]
    dx = p[0] - X
    dy = p[1] - Y
    return (dx ** 2 + dy ** 2)**0.5


exec(input().strip())  # must have this line when submitting to grader
