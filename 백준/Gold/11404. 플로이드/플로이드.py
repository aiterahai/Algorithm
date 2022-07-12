from sys import stdin
from collections import deque

INF = int(1e9)
N = int(stdin.readline())
board = [[INF for i in range(N + 1)] for j in range(N + 1)]
M = int(stdin.readline())
for i in range(1, N + 1): board[i][i] = 0
for i in range(M):
    A, B, C = map(int, stdin.readline().split())
    board[A][B] = min(board[A][B], C)
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if board[i][j] == INF: print(0, end=" ")
        else: print(board[i][j], end=" ")
    print()