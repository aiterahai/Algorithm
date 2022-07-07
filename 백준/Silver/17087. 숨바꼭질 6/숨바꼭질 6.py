from math import gcd
from sys import stdin

N, S = map(int, stdin.readline().split())
board = list(map(int, stdin.readline().split()))
for i in range(len(board)): board[i] = abs(board[i] - S)

m = board.pop()
for i in board: m = gcd(m, i)
print(m)