import numpy as np

def sum_2_rows(M):
    # return summation in each column of 2 adjacent rows
    return M[::2, ::] + M[1::2, ::]


def sum_left_right(M):
    # return summation of left half and right half
    n = int(M.shape[1] / 2)
    return M[::, :n:] + M[::, n::]


def sum_upper_lower(M):
    # return summation of upper half and lower half
    n = int(M.shape[0] / 2)
    return M[:n:, ::] + M[n::, ::]


def sum_4_quadrants(M):
    # return summation in the same position from 4 quadrants
    n0 = int(M.shape[0] / 2)
    n1 = int(M.shape[1] / 2)
    out = np.zeros([n0, n1], int)
    for i in range(n0):
        for j in range(n1):
            out[i, j] = np.sum(M[i::n0, j::n1])

    return out


def sum_4_cells(M):
    # return summation of 4 adjacent numbers
    n0 = int(M.shape[0] / 2)
    n1 = int(M.shape[1] / 2)
    temp = []
    for i in range(0, M.shape[0], 2):
        for j in range(0, M.shape[1], 2):
            temp.append(np.sum(M[i:i + 2, j:j + 2]))

    return np.array(temp).reshape(n0, n1)


def count_leap_years(years):
    # years is array which contains Buddhist years
    # return number of leap years
    # (y % 400 == 0)
    # (y % 4 == 0 and y % 100 != 0)
    temp = []
    for y in years:
        if ((y - 543) % 400 == 0):
            temp.append(y)
        elif ((y - 543) % 4 == 0 and (y - 543) % 100 != 0):
            temp.append(y)
            
    return len(temp)


exec(input().strip())  # This command is necessary to grade your answer
