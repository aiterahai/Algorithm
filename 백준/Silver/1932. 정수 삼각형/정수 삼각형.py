from sys import stdin

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) + [0] * (5 - i) for i in range(1, N + 1)]
result = [[0 for _ in range(N)] for _ in range(N)]
result[0][0] = board[0][0]
for i in range(1, N):
    for j in range(i + 1):
        result[i][j] = max(result[i-1][j], result[i-1][j-1]) + board[i][j]
print(max(map(max, result)))