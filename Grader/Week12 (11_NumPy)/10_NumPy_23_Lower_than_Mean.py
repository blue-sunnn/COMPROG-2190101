import numpy as np

def read_data():
    # Read data from input, then create and return 2 arrays
    # weight is array with the size of 3, contain weight of midterm, final, and project score (float)
    # data is array with nx4 shape, contain data of each n number of student, each consist of
    # student ID, midterm socre, final score, and project score (int)
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data


def report_lower_than_mean(weight, data):
    # Show Student IDs of students with average score lower than mean
    # Show all IDs on the single line with ", " in between (a comma and one space)
    # Arrange in order appear in data if no student has average score lower than mean, show 'None'
    scores = np.sum(weight * data[::, 1::], axis=1)
    mean = np.mean(scores)
    m = (scores < mean)

    if int(np.sum(scores[scores < mean])) == 0:
        print('None')
    else:
        toShow = (data[m][:, :1])
        jaShow = toShow.reshape(1, toShow.shape[0])[0].tolist()
        print(', '.join([str(e) for e in jaShow]))


exec(input().strip())  # You must have this line when submit to grader
