"""
file name: 9465.py

create time: 2023-04-10 19:02
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    board = [list(map(int, stdin.readline().split())) for _ in range(2)]
    for i in range(1, N):
        if i == 1: board[0][1], board[1][1] = board[0][1] + board[1][0], board[1][1] + board[0][0]
        else:
            board[0][i] += max(board[1][i - 1], board[1][i - 2])
            board[1][i] += max(board[0][i - 1], board[0][i - 2])

    print(max(board[0][-1], board[1][-1]))