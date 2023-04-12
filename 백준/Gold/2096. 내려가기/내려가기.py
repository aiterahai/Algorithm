"""
file name: 2096.py

create time: 2023-04-11 22:01
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
table = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(2)]
table[0][0], table[1][0] = board[0].copy(), board[0].copy()
for i in range(1, N):
    j = i % 2
    table[0][j] = [board[i][k] + max(*table[0][j - 1][max(k - 1, 0) : k + 2]) for k in range(3)]
    table[1][j] = [board[i][k] + min(*table[1][j - 1][max(k - 1, 0) : k + 2]) for k in range(3)]
print(max(table[0][N % 2 - 1]), min(table[1][N % 2 - 1]))