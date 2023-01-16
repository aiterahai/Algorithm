from sys import stdin

board = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    for i in range(x - 1, x + 9):
        for j in range(y - 1, y + 9):
            board[i][j] = 1

print(sum([sum(i) for i in board]))