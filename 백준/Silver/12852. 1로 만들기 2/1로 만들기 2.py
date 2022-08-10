from sys import stdin

N = int(stdin.readline())
dp, route = [0] * (N + 1),  [0] * (N + 1)
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    route[i] = i - 1
    if i % 2 == 0:
        if dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            route[i] = i // 2
    if i % 3 == 0:
        if dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            route[i] = i // 3
print(dp[N])
node = N
while node:
    print(node, end=" ")
    node = route[node]