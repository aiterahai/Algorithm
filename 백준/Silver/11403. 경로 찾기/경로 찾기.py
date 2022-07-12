from sys import stdin

INF = int(1e9)
N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for i in range(N)]
for i in range(N):
    for j in range(N):
        if not board[i][j]: board[i][j] = INF
for k in range(N):
    for i in range(N):
        for j in range(N):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])
for i in range(N):
    for j in range(N):
        if board[i][j] == INF: print(0, end=" ")
        else: print(1, end=" ")
    print()