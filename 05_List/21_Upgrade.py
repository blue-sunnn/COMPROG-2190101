aup = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
ids, grades = [], []

x = input().split()
while x != ['q']:
    ids.append(x[0])
    grades.append(x[1])
    x = input().split()

uids = input().split()
# new grade = index of old grade - 1
for i in uids:
    grades[ids.index(i)] = aup[max(0, aup.index(grades[ids.index(i)]) - 1)]
for j in range(len(ids)):
    print(ids[j], grades[j])
