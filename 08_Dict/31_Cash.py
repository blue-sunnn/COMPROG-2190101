def total(pocket):
    return sum([val * price for price, val in pocket.items()])


def take(pocket, money_in):
    for price, val in money_in.items():
        if price not in pocket.keys():
            pocket[price] = val
        else:
            pocket[price] += val


def pay(pocket, amt):
    d = {}
    if total(pocket) < amt:
        return {}
    for k in sorted(pocket)[::-1]:
        if (amt // k) * k >= pocket[k] * k:
            p = pocket[k] * k
            amt -= p
            d[k] = p // k
        elif (amt // k) * k > 0:
            p = (amt // k) * k
            amt -= p
            d[k] = p // k
    if amt > 0:
        return {}
    else:
        for i in d:
            pocket[i] -= d[i]
        return d


exec(input().strip())  # must have this line when submitting to grader
