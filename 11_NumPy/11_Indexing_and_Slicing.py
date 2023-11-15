import numpy as np
# A is a 2-d array
def get_column_from_bottom_to_top(A, c):
    return A.T[::-1, ::-1][c - 1]


def get_odd_rows(A):
    return A[1::2]


def get_even_column_last_row(A):
    return A[-1::, ::2][0]


def get_diagonal1(A):  # A is a square matrix
    # from top-left corner down to bottom-right corner
    return np.array([A[i, j] for i in range(A.shape[0]) for j in range(A.shape[1]) if i == j])


def get_diagonal2(A):  # A is a square matrix
    # from top-right corner down to bottom-left corner
    return get_diagonal1(A.T[::-1])


exec(input().strip())  # must have this line when submitting to grader
