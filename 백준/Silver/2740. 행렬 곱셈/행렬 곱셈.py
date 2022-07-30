from sys import stdin

N, M = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for i in range(N)]
M, K = map(int, stdin.readline().split())
B = [list(map(int, stdin.readline().split())) for i in range(M)]
board = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            board[i][j] += A[i][k] * B[k][j]

for i in board: print(*i)