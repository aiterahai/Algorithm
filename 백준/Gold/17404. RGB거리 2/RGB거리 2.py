"""
file name: 17404.py

create time: 2023-04-18 11:56
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
INF = int(1e9)

answer = INF
for i in range(3):
    table = [[INF, INF, INF] for _ in range(N)]
    table[0][i] = board[0][i]
    for j in range(1, N):
        table[j][0] = board[j][0] + min(table[j - 1][1], table[j - 1][2])
        table[j][1] = board[j][1] + min(table[j - 1][0], table[j - 1][2])
        table[j][2] = board[j][2] + min(table[j - 1][0], table[j - 1][1])

    for j in range(3):
        if i != j:
            answer = min(answer, table[N - 1][j])

print(answer)