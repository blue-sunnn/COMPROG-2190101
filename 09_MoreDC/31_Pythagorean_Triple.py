def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(a, b, c):
    # return whether a, b, c is coprime or not, return as boolean
    # read a definition of coprime here
    if gcd(a, b) == 1: return True
    if gcd(a, c) == 1: return True
    if gcd(b, c) == 1:return True
    return False


def primitive_Pythagorean_triples(max_len):
    # return a list contain sublists of 3 values of a, b, c
    # a < b < c < max_len
    # each sublists are arrange by c from lowest to greatest number
    # if c has same value, arrange by a
    triple = []
    for c in range(max_len + 1):
        for b in range(c):
            for a in range(b):
                if (c ** 2 == (a ** 2) + (b ** 2)) and is_coprime(a, b, c): triple.append([a, b, c])
                
    temp = sorted([[i[2], i[0], i[1]] for i in triple])
    triple = [[i[1], i[2], i[0]] for i in temp]
    return triple


exec(input().strip())  # this line is required for grader to work.
