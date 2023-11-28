class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a == self.b == 0:       return str(0)
        if self.a != 0 and self.b == 0: return str(self.a)
        if self.a == 0:
            if self.b == -1:    return '-i'
            elif self.b == 1:   return 'i'
            else:               return str(self.b) + 'i'
        if self.a != 0 and self.b != 0:
            s = str(self.a)
            if self.b == -1:    s += '-'
            elif self.b == 1:   s += '+'
            elif self.b < 0:    s += str(self.b)
            elif self.b > 0:    s += '+' + str(self.b)
            return s + 'i'

    def __add__(self, rhs):
        a = self.a + rhs.a
        b = self.b + rhs.b
        return Complex(a, b)

    def __mul__(self, rhs):
        a = (self.a * rhs.a) - (self.b * rhs.b)
        b = (self.a * rhs.b) + (self.b * rhs.a)
        return Complex(a, b)

    def __truediv__(self, rhs):
        a = ((self.a * rhs.a) + (self.b * rhs.b)) / (rhs.a**2 + rhs.b**2)
        b = (-(self.a * rhs.b) + (self.b * rhs.a)) / (rhs.a**2 + rhs.b**2)
        return Complex(a, b)


t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if t == 1:      print(c1)
elif t == 2:    print(c2)
elif t == 3:    print(c1 + c2)
elif t == 4:    print(c1 * c2)
else:           print(c1 / c2)
