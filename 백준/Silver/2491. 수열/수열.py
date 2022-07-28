from sys import stdin

N = int(stdin.readline())
board = list(map(int, stdin.readline().split()))
board = [1 if board[i + 1] > board[i] else (-1 if board[i + 1] < board[i] else 0) for i in range(N - 1)]
answer, M, m = 0, 0, 0
for i in board:
    if i == 1: M, m = M + 1, 0; answer = max(answer, M, m)
    elif i == -1: M, m = 0, m + 1; answer = max(answer, M, m)
    else: M, m = M + 1, m + 1; answer = max(answer, M, m)
print(answer + 1)