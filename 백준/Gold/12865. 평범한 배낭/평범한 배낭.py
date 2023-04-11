"""
file name: 12865.py

create time: 2023-04-11 14:35
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

N, K = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
table = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        w, v = board[i - 1]
        if j < w: table[i][j] = table[i - 1][j]
        else: table[i][j] = max(v + table[i - 1][j - w], table[i - 1][j])

print(max(map(max, table)))