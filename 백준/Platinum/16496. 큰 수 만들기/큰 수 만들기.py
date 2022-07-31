from sys import stdin

N = int(stdin.readline())
board = list(stdin.readline().split())
for i in range(N):
    for j in range(N - 1):
        if int(board[j] + board[j + 1]) < int(board[j + 1] + board[j]): board[j + 1], board[j] = board[j], board[j + 1]
if max(map(int, board)) == 0: print(0)
else: print(*board, sep="")