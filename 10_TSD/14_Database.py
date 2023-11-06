courses = {}
f = open(input().strip())
for line in f:
    n, id = [i.strip() for i in line.split(',')]
    courses[n] = id
f.close()

teachers = {}
f = open(input().strip())
for line in f:
    n, name = [i.strip() for i in line.split(',')]
    teachers[n] = name
f.close()

f = open(input().strip())
for line in f:
    x, y = [i.strip() for i in line.split(',')]
    if x in courses and y in teachers:
        print(courses[x] + ',' + teachers[y])
    else:
        print('record error')
f.close()
