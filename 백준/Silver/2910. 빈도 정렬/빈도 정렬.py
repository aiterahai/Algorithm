from sys import stdin

N, M = map(int, stdin.readline().split())
temp = list(map(int, stdin.readline().split()))
board = {}
for i in temp: board[i] = board.get(i, 0) + 1
board = list(zip(board.values(), board.keys()))
for i, j in sorted(board, key = lambda x:(x[0]), reverse=True): print(f"{j} " * i, end="")