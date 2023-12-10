import math

w = float(input())
h = float(input())

Mosteller_Formula = ((w * h) ** 0.5)/60
Haycock_F = 0.024265 * (w ** 0.5378) * (h ** 0.3964)
Boyd_F = 0.0333 * w ** ((0.6157 - (0.0188 * math.log(w, 10)))) * (h ** 0.3)

print(Mosteller_Formula)
print(Haycock_F)
print(Boyd_F)
