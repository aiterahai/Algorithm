dp = [0 for _ in range(41)]
dp[1], dp[2] = 1, 1
for i in range(3, 41): dp[i] = dp[i-1] + dp[i-2]
N = int(input())
print(dp[N], N-2)