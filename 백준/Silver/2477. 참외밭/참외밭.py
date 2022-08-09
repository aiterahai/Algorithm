from sys import stdin
K = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(6)]
Mw = max([j for i, j in board if i == 1 or i == 2])
Mh = max([j for i, j in board if i == 3 or i == 4])
mw = abs(board[[i[1] for i in board].index(Mw) - 1][1] - board[([i[1] for i in board].index(Mw) + 1) % 6][1])
mh = abs(board[[i[1] for i in board].index(Mh) - 1][1] - board[([i[1] for i in board].index(Mh) + 1) % 6][1])
print((Mw * Mh - mw * mh) * K)