def is_prime(n):
    # Check if n is a prime number
    if n <= 1:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True


def next_prime(n):
    # Return the least prime number which is more than n
    n += 1
    while not (is_prime(n)):
        n += 1
    return n


def next_twin_prime(n):
    # Return the least twin prime number which is more than n
    # twin prime number are 2 prime numbers differed by 2
    n += 1
    while not (is_prime(n) and is_prime(n + 2)):
        n += 1
    return n, n + 2


exec(input().strip())
