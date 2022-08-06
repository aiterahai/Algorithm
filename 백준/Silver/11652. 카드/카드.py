from sys import stdin

N = int(stdin.readline())
temp = [int(stdin.readline()) for i in range(N)]
board = {}
for i in temp: board[i] = board.get(i, 0) + 1
print(sorted([[i, j] for i, j in zip(board.values(), board.keys())], key = lambda x:(x[0], -x[1]))[-1][1])