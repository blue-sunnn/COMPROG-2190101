animals = {}
a, b = [], []

while True:
    t = input().split(', ')
    if t[0] == 'q': break
    
    a.append(t[0])
    if t[1] not in b: b.append(t[1])

    name, toa = t
    if toa not in animals: animals[toa] = [name]
    else:                  animals[toa] += [name]

for i in b: print(i + ': ' + ', '.join([e for e in a if e in animals[i]]))
