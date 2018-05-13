# exercise for Class type in Python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)
    def __div__(self, r):
        return Rational(self.p * r.q , self.q * r.p)
    def __int__(self):
        return self.p // self.q
    def __float__(self):
        return self.p / self.q
    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)
    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print (r1 + r2)
print (r1 - r2)
print (r1 * r2)
print (r1 / r2)
print (float(Rational(7, 2)))
print (float(Rational(1, 3)))
