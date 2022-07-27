from sys import stdin

N = int(stdin.readline())
board = sorted(list(map(int, stdin.readline().split())))
print(board[-1] + sum(board[:-1]) / 2)