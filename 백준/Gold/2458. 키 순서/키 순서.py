from sys import stdin

N, M = map(int, stdin.readline().split())
board = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(M):
    A, B = map(int, stdin.readline().split())
    board[A][B] = 1
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][k] and board[k][j]: board[i][j] = 1
answer = [0 for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if board[i][j]: answer[i], answer[j] = answer[i] + 1, answer[j] + 1
print(answer.count(N - 1))