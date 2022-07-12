from sys import stdin

INF = int(1e9)
N = int(stdin.readline())
board = [[INF for i in range(N)] for j in range(N)]
for i in range(N): board[i][i] = 0
while True:
    A, B = map(int, stdin.readline().split())
    if A == -1 and B == -1: break
    board[A - 1][B - 1], board[B - 1][A - 1] = 1, 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])
total = min(map(max, board))
maxs = list(map(max, board))
result = []
for i in range(N):
    if maxs[i] == total:
        result.append(i + 1)
print(total, len(result))
print(*result)