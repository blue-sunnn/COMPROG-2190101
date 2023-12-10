def checkDNA(dna):
    code = ['A', 'T', 'C', 'G']
    for i in dna:
        if i not in code:
            return False
    return True


def rDNA(dna):
    p1, p2 = ['A', 'C'], ['T', 'G']
    rDna = ''
    for i in dna[::-1]:
        if i in p1: rDna += p2[p1.index(i)]
        else:       rDna += p1[p2.index(i)]
    print(rDna)


def fCode(dna):
    print('A=' + str(dna.count('A')) + ', T=' + str(dna.count('T')) +
          ', G=' + str(dna.count('G')) + ', C=' + str(dna.count('C')))


def dDNA(dna):
    c = 0
    p = input()
    for i in range(len(dna) - 1):
        if dna[i:i + 2] == p:
            c += 1
    print(c)


dna = input().upper().strip()
op = input()

if checkDNA(dna):
    if op == 'R': rDNA(dna)
    if op == 'F': fCode(dna)
    if op == 'D': dDNA(dna)
else:
    print('Invalid DNA')
