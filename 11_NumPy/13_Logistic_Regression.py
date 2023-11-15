import numpy as np

def p(x):
    # x is an array with size n x 2, containing the number of
    # problems solved (column 0), and GPA (column 1) of n students
    #
    # Return an array with size n, containing the probability
    # student will pass the course, calculated with the formula above.
    #
    # Using NumPy, will allow you to write this function without
    # using loops. (The answer is no more than 3 lines)
    x0, x1 = x[:, 0], x[:, 1]
    logit = -3.98 + (0.1 * x0) + (0.5 * x1)
    return (1 / (1 + np.e ** (-logit)))


exec(input().strip())  # This line is required for Grader to work.
