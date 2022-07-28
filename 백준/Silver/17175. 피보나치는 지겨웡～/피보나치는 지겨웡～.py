dp = [1, 1]
N = int(input())
for i in range(N): dp[i%2] = (sum(dp) + 1) % 1000000007
print(dp[N%2])