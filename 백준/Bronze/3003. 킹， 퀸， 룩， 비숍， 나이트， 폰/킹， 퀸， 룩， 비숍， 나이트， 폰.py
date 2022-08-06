from sys import stdin

board = list(map(int, stdin.readline().split()))
for i, j in zip(board, [1, 1, 2, 2, 2, 8]): print(j - i, end=" ")