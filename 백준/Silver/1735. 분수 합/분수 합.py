from fractions import Fraction
from sys import stdin

A, B = Fraction(*map(int, stdin.readline().split())), Fraction(*map(int, stdin.readline().split()))
print((A + B).numerator, (A + B).denominator)