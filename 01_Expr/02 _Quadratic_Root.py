a = float(input())
b = float(input())
c = float(input())

x = ((b ** 2) - (4 * a * c)) ** 0.5

print(round(((-b - x)/(2 * a)), 3))
print(round(((-b + x)/(2 * a)), 3))