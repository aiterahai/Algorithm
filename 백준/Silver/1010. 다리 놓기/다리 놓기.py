from math import factorial
from sys import stdin
for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    print(factorial(M) // (factorial(N) * factorial(M - N)))