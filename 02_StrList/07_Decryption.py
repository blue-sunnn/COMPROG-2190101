alp_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

n = input()

a = n[3::7]
b = n[7::5]
c = str(int(a) + int(b) + 10000)
d = c[-4:-1]
e = str(int(d[0]) + int(d[1]) + int(d[2]))
e = int(e[-1:]) + 1
f = alp_list[e - 1]

print(d + f)