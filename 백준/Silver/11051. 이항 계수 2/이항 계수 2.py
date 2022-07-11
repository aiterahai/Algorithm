from sys import stdin
from fractions import Fraction
from math import factorial

N, K = map(int, stdin.readline().split())
print(Fraction(factorial(N), factorial(K) * factorial(N - K)) % 10007)