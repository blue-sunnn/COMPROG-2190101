import math

n = int(input())

x = (2 * math.pi) ** 0.5
y = n ** (n + 1/2)

print(x * y * (math.e) ** (-n + 1/(12 * n + 1)))
print(x * y * (math.e) ** (-n + 1/(12 * n)))
