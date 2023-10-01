aup = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
ids, grades, mtl = [], [], []

x = input().split()
while x != ['q']:
    ids.append(x[0])
    grades.append(x[1])
    x = input().split()

uids = input().split()

for i in uids:
    grades[ids.index(i)] = aup[max(0, aup.index(grades[ids.index(i)]) - 1)]
    
for j in range(len(ids)):
    y = []
    y.append(ids[j])
    y.append(grades[j])
    mtl.append(y)  # append [ids, grade] of each student in new list

mtl.sort()  # sort by the first element of each list in mtl
for k in mtl:
    print(k[0], k[1])
