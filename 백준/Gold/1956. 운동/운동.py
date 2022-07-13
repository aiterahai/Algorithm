from sys import stdin

INF = int(1e9)
V, E = map(int, stdin.readline().split())
board = [[INF for i in range(V)] for j in range(V)]
for i in range(E):
    A, B, C = map(int, stdin.readline().split())
    board[A-1][B-1] = C
for k in range(V):
    for i in range(V):
        for j in range(V):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])
answer = INF
for i in range(V): answer = min(answer, board[i][i])
if answer == INF: print(-1)
else: print(answer)