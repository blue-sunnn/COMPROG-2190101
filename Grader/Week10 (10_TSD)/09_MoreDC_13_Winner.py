winner, loser = [], []

for _ in range(int(input())):
    w, l = input().split()
    winner.append(w)
    loser.append(l)

print(sorted(set(winner) - set(loser)))
