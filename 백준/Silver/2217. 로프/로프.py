from sys import stdin

N = int(stdin.readline())
board = sorted([int(stdin.readline()) for i in range(N)], reverse=True)
result = 0
for i in range(1, N + 1): result = max(board[i - 1] * i, result)
print(result)