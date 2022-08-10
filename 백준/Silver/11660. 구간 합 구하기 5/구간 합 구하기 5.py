from sys import stdin

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + board[i][j]
for _ in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(dp[x2 - 1][y2 - 1] - (dp[x1 - 2][y2 - 1] + dp[x2 - 1][y1 - 2] - dp[x1 - 2][y1 - 2]))