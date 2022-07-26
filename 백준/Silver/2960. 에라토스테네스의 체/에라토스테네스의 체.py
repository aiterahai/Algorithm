N, K = map(int, input().split())
board = [1 for i in range(N + 1)]
for i in range(2, N + 1):
    if not board[i]: continue
    for j in range(i, N + 1, i):
        if board[j]:
            board[j], K = 0, K - 1
            if K == 0:
                print(j)