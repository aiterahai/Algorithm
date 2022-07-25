from sys import stdin
from math import gcd

N = int(stdin.readline())
board = [int(stdin.readline()) for i in range(N)]
diff = [board[i] - board[i-1] for i in range(1, N)]
print((board[-1] - board[0]) // gcd(*diff) - N + 1)