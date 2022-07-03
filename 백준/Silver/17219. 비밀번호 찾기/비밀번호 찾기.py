from sys import stdin

board = {}
N, M = map(int, stdin.readline().split())
for i in range(N):
    info = stdin.readline().split()
    board[info[0]] = info[1]
for i in range(M):
    info = stdin.readline()[:-1]
    print(board[info])