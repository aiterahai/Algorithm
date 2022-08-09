from sys import stdin

N = int(stdin.readline())
board = [int(stdin.readline()) for i in range(N)]
dp = [[0, 0, 0] for i in range(N)]
dp[0] = [0, board[0], 0]
for i in range(1, N):
    dp[i] = [max(dp[i - 1]), dp[i - 1][0] + board[i], dp[i - 1][1] + board[i]]
print(max(dp[-1]))