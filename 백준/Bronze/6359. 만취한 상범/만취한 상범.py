from sys import stdin

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    board = [True] * (N + 1)
    for i in range(2, N + 1):
        for j in range(i, N + 1, i):
            board[j] = not board[j]
    print(sum(board) - 1)