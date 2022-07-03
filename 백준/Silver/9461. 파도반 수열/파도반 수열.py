from sys import stdin

T = int(stdin.readline())
dp = [0, 1, 1, 1]
for i in range(4, 101): dp.append(dp[i-2] + dp[i-3])
for i in range(T): print(dp[int(stdin.readline())])