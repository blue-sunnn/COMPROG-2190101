temp, toShow = {}, []

for i in range(int(input())):
    song, singer, genre, t = input().split(', ')
    m, s = t.split(':')
    t = (int(m) * 60) + int(s)
    if genre not in temp: temp[genre] = t
    else:                 temp[genre] += t

for i in sorted([[v, k] for k, v in temp.items()], reverse=True):
    if i[0] < 60:
        toShow.append(str(i[1]) + ' --> ' + str(i[0]))
    else:
        m = i[0] // 60
        s = i[0] % 60
        if s < 10: s = '0' + str(s)
        else:      s = str(s)
        toShow.append(str(i[1]) + ' --> ' + str(m) + ':' + s)

for i in toShow[:3]: print(i)
