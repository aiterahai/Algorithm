from sys import stdin

N = int(stdin.readline())
board = list(map(int, stdin.readline().split()))
dp = [1]
for i in range(1, N): dp.append(max([1] + [dp[j] + 1 for j in range(len(dp)) if board[i] > board[j]]))
print(max(dp))