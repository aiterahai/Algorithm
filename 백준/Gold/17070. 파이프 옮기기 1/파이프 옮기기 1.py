"""
file name: 17070.py

create time: 2023-04-12 11:52
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

table = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

table[0][0][1] = 1

for i in range(2, N):
    if board[0][i] == 0:
        table[0][0][i] = table[0][0][i - 1]

for x in range(1, N):
    for y in range(1, N):
        if board[x][y]: continue
        table[0][x][y] = table[0][x][y - 1] + table[2][x][y - 1]
        table[1][x][y] = table[1][x - 1][y] + table[2][x - 1][y]
        if board[x - 1][y] or board[x][y - 1]: continue
        table[2][x][y] = table[0][x - 1][y - 1] + table[1][x - 1][y - 1] + table[2][x - 1][y - 1]

print(sum(table[i][-1][-1] for i in range(3)))