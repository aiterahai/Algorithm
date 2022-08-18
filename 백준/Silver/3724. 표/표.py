from sys import stdin

for _ in range(int(stdin.readline())):
    M, N = map(int, stdin.readline().split())
    board = list(zip(*[list(map(int, stdin.readline().split())) for _ in range(N)]))
    for i in range(M):
        temp = 1
        for j in range(N):
            temp *= board[i][j]
        board[i] = temp
    print(M - board[::-1].index(max(board)))