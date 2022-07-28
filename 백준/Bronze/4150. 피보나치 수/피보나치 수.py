from sys import stdin

N = int(stdin.readline())
dp = [0, 1]
for i in range(N): dp[i%2] = sum(dp)
print(dp[N%2])