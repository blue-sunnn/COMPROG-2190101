u = input()
v = input()

# cut (), split string, change it to be float, and keep it in list
u = list(map(float, u[1:-1].split(', ')))
v = list(map(float, v[1:-1].split(', ')))

s = [u[0] + v[0], u[1] + v[1], u[2] + v[2]]

print(str(u) + ' + ' + str(v) + ' = ' + str(s))
