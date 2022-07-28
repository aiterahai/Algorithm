N, dp = int(input()), [0, 1]
for i in range(N): dp[i%2] = sum(dp) % 1000000007
print(dp[N % 2])