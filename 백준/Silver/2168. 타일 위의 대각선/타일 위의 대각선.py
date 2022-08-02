from math import gcd
from sys import stdin

x, y = map(int, stdin.readline().split())
print(x + y - gcd(x, y))