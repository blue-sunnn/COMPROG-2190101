def reverse(d):
    # d is a dict that has no repeated value
    # returns new dict that store key, value as value, key of d
    temp = {d[k]: k for k in d}
    return temp


def keys(d, v):
    # returns a list of keys in d (can be in any order) that
    # have a value of v
    temp = [k for k in d if d[k] == v]
    return temp


exec(input().strip())  # must have this line when submitting to grader
