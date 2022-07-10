dp = [0, 1] + [0] * 50000
for i in range(2, 50001):
    result = 4
    j = 1
    while i >= j ** 2: result, j = min(result, dp[i-j**2]), j + 1
    dp[i] = result + 1
print(dp[int(input())])