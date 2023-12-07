import numpy as np

# Function 1
def generate_followed_by_dict(infile):
    # write your code here
    followed_by = {}
    f = open(infile)
    for line in f:
        x = line.strip().split(',')
        followed_by[x[0]] = x[1:]
    f.close()

    return followed_by

# Function 2
def generate_followed_by_matrix(followed_by_dict):
    # write your code here
    names = list(followed_by_dict.keys())
    for e in followed_by_dict.values(): names += e
    names = sorted(list(set(names)))

    m = np.zeros([len(names), len(names)], int)
    for person, follower in followed_by_dict.items():
        for ppl in follower:
            m[names.index(person), names.index(ppl)] = 1

    return m, names

# Function 3
def generate_degree_matrix(A):
    # write your code here
    m = np.identity(A.shape[0], int) * np.sum(A, axis = 1)
    return m

# Function 4
def get_top_influencer(M, person_names):
    # write your code here
    M_sum = np.sum(M, axis = 1)
    M_max = np.max(M_sum)
    names = np.array(person_names)
    return list(names[M_sum == M_max])

def tanimoto_coefficient(a, b):
    sum_a, sum_b = np.sum(a), np.sum(b)
    bi_A, bi_B = a == 1, b == 1
    compareAB = (bi_A & bi_B) * 1
    c = np.sum(compareAB)
    return round(c / (sum_a + sum_b - c), 2)

# Function 5
def generate_similarity_matrix_among_influencers(M, person_names):
    # write your code here
    M_sum = np.sum(M, axis = 1)
    remove_0 = M[M_sum > 0]
    out = np.zeros((remove_0.shape[0], remove_0.shape[0]), float)
    for i in range(remove_0.shape[0]):
        for j in range(remove_0.shape[0]):
            if i != j:
                out[i, j] = tanimoto_coefficient(remove_0[i], remove_0[j])

    names = np.array(person_names)

    return out, names[M_sum > 0]

# Function 6
def  get_all_pairs_of_most_similar_influencers(S, only_influencers):
    # write your code here
    S_max = np.max(S)
    if S_max == 0: return []
    out = []
    for i in range(len(only_influencers)):
        for j in range(len(only_influencers)):
            if S[i, j] == S_max:
                if (i, j) not in out and (j, i) not in out:
                    out.append((i, j))

    return [(only_influencers[ii], only_influencers[jj]) for ii, jj in out]