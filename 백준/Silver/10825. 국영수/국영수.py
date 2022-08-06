from sys import stdin

N = int(stdin.readline())
board = [list(stdin.readline().split()) for i in range(N)]
for i in range(N): board[i][1], board[i][2], board[i][3] = map(int, [board[i][1], board[i][2], board[i][3]])
board = sorted(board, key = lambda x:(-x[1], x[2], -x[3], x[0]))
for i in board: print(i[0])