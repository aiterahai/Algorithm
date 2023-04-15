"""
file name: 2448.py

create time: 2023-04-15 14:51
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

N = int(stdin.readline())
board = [[False] * 2 * N for _ in range(N)]
def recursion(x, y, N):
    if N == 3:
        board[x][y] = True
        board[x + 1][y - 1] = board[x + 1][y + 1] = True
        for i in range(-2, 3):
            board[x + 2][y + i] = True
    else:
        recursion(x, y, N // 2)
        recursion(x + N // 2, y - N // 2, N // 2)
        recursion(x + N // 2, y + N // 2, N // 2)

recursion(0, N - 1, N)
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j]: print("*", end="")
        else: print(" ", end="")
    print()