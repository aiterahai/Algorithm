from sys import stdin

dp = [1] + [0] * 35
for i in range(1, 36):
    for j in range(i): dp[i] += dp[j] * dp[i - j - 1]
print(dp[int(stdin.readline())])