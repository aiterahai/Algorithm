from sys import stdin

INF = int(1e9)
N = int(stdin.readline())
M = int(stdin.readline())
board = [[INF for i in range(N + 1)] for j in range(N + 1)]
next = [[0 for i in range(N + 1)] for j in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, stdin.readline().split())
    board[a][b] = min(board[a][b], c)
    next[a][b] = b
for i in range(1, N + 1): board[i][i] = 0
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]
                next[i][j] = next[i][k]
for i in board[1:]:
    for j in i[1:]:
        if j >= INF: print(0, end=" ")
        else: print(j, end=" ")
    print()
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if not board[i][j] or board[i][j] == INF: print(0); continue
        result = []
        x = i
        while x != j:
            result.append(x)
            x = next[x][j]
        result.append(j)
        print(len(result), *result)