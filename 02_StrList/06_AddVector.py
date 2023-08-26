u = input()
v = input()

u = list(map(float, u[1:-1].split(', ')))
v = list(map(float, v[1:-1].split(', ')))

sum = [u[0] + v[0], u[1] + v[1], u[2] + v[2]]

print(str(u) + ' + ' + str(v) + ' = ' + str(sum))