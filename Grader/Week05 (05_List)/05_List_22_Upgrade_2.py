aup = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
ids, grades, mtl = [], [], []

x = input().split()
while x != ['q']:
    ids.append(x[0])
    grades.append(x[1])
    x = input().split()

for i in input().split():
    grades[ids.index(i)] = aup[max(0, aup.index(grades[ids.index(i)]) - 1)]
    
for j in range(len(ids)):
    mtl.append([ids[j], grades[j]]) 

for k in sorted(mtl):
    print(k[0], k[1])
