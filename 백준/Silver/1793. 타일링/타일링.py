from sys import stdin

dp = [1, 1, 3] + [0 for i in range(248)]
for i in range(3, 251):
    dp[i] = dp[i - 1] + dp[i - 2] * 2
while True:
    try:
        print(dp[int(stdin.readline())])
    except:
        break