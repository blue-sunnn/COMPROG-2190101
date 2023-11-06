temp = {}
for i in range(int(input())):
    song, singer, genre, t = input().split(', ')
    m, s = t.split(':')
    t = (int(m) * 60) + int(s)
    if genre not in temp:
        temp[genre] = t
    else:
        temp[genre] += t

temp1 = sorted([[v, k] for k, v in temp.items()], reverse=True)
toShow = []
for i in temp1:
    if i[0] < 60:
        toShow.append(str(i[1]) + ' --> ' + str(i[0]))
    else:
        m = i[0] // 60
        s = i[0] % 60
        m = str(m)
        if s < 10:
            s = '0' + str(s)
        else:
            s = str(s)
        toShow.append(str(i[1]) + ' --> ' + m + ':' + s)

for i in toShow[:3]:
    print(i)
