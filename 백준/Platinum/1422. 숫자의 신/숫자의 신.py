from sys import stdin

K, N = map(int, stdin.readline().split())
board = sorted([int(stdin.readline()) for i in range(K)], key=lambda x:(len(str(x)), x), reverse=True)
board = list(map(str, [board[0]] * (N - K + 1) + board[1:]))
for i in range(N):
    for j in range(N - 1):
        if int(board[j] + board[j + 1]) < int(board[j + 1] + board[j]):
            board[j], board[j + 1] = board[j + 1], board[j]
print(*board, sep="")