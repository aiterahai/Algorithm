from sys import stdin

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    board = list(map(int, stdin.readline().split()))
    dp = [board[0]] + [0 for i in range(N - 1)]
    for i in range(1, N): dp[i] = max(board[i], board[i] + dp[i - 1])
    print(max(dp))