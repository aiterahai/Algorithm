N = int(input())
INF = int(1e9)
board = list(map(int, input().split()))
dp = [board[0]] + [-INF for _ in range(N)]
for i in range(1, N): dp[i] = max(dp[i-1] + board[i], board[i])
print(max(dp))