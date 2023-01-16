from sys import stdin

board = [list(map(int, stdin.readline().split())) for _ in range(9)]
M = max(map(max, board))
print(M)
print(list(map(max, board)).index(M) + 1, board[list(map(max, board)).index(M)].index(M) + 1)