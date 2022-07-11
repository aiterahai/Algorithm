from sys import stdin
N = int(stdin.readline())
board = [0] + [int(stdin.readline()) for i in range(N)]
dp = [0 for i in range(N + 1)]
if N == 1:
    print(board[1])
    exit(0)
if N == 2:
    print(board[1] + board[2])
    exit(0)
dp[1] = board[1]
dp[2] = board[1] + board[2]
dp[3] = max(board[1] + board[3], board[2] + board[3])
for i in range(4, N + 1): dp[i] = max(board[i] + dp[i - 2], dp[i - 3] + board[i - 1] + board[i])
print(dp[N])