from sys import stdin

N = int(stdin.readline())
board = [float(stdin.readline()) for i in range(N)]
dp = [board[0]] + [0 for i in range(N - 1)]
for i in range(1, N): dp[i] = max(dp[i - 1] * board[i], board[i])
print(f"{max(dp):.3f}")