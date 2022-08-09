from math import gcd
from sys import stdin

N = int(stdin.readline())
board = sorted([int(stdin.readline()) for i in range(N)])
M = gcd(*[board[i + 1] - board[i] for i in range(N - 1)])
result = []
for i in range(1, int(M ** 0.5) + 1):
    if M % i: continue
    result.append(i)
    result.append(M // i)
print(*sorted(list(set(result)))[1:])