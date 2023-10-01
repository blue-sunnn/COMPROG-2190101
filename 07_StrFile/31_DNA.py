def chechDNA(dna):
    code = ['A', 'T', 'C', 'G']
    for i in dna:
        if i not in code:
            return False
    return True


def rDNA(dna):
    p1, p2 = ['A', 'C'], ['T', 'G']
    dna = dna[::-1]
    rDna = ''
    for i in dna:
        if i in p1:
            rDna += p2[p1.index(i)]
        else:
            rDna += p1[p2.index(i)]
    print(rDna)


def fCode(dna):
    a, t, c, g = 0, 0, 0, 0
    for i in dna:
        if i == 'A': a += 1
        elif i == 'T': t += 1
        elif i == 'C': c += 1
        elif i == 'G': g += 1
    print('A=' + str(a) + ', T=' + str(t) + ', G=' + str(g) + ', C=' + str(c))


def dDNA(dna):
    c = 0
    p = input()
    for i in range(len(dna) - 1):
        if dna[i:i + 2] == p:
            c += 1
    print(c)


dna = input().upper().strip()
op = input()

if chechDNA(dna):
    if op == 'R': rDNA(dna)
    if op == 'F': fCode(dna)
    if op == 'D': dDNA(dna)
else:
    print('Invalid DNA')
