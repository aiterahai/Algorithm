from fractions import Fraction
from math import factorial

n, m = map(int, input().split())
print(Fraction(factorial(n), factorial(n - m) * factorial(m)))