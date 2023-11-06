dep_info = {}
for _ in range(int(input())):
    x = input().split()
    dep_info[x[0]] = int(x[1])

stu_info = []
for _ in range(int(input())):
    x = input().split()
    stu_info.append([float(x[1]), x[0], x[2:]])

result = {}
for score, sid, de in sorted(stu_info)[::-1]:
    for i in de:
        if dep_info[i] > 0:
            dep_info[i] -= 1
            result[sid] = i
            break

for i, j in sorted(result.items()):
    print(i, j)
