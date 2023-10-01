def make_int_list(x):
    # x is string and convert it to int in list
    return list(map(int, x.split()))


def is_odd(e):
    # check if e is odd or not
    return e % 2 != 0


def odd_list(alist):
    # return list of odd numbers
    x = []
    for i in alist:
        if i % 2 != 0: x.append(i)
    return x


def sum_square(alist):
    # sum of square of each number in list
    x = 0
    for i in alist:
        x += i ** 2
    return x


exec(input().strip())
