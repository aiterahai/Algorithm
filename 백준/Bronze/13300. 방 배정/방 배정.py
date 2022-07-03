from sys import stdin

N, K = map(int, stdin.readline().split())
board = [0 for i in range(12)]
count = 0
for i in range(N):
    S, Y = map(int, stdin.readline().split())
    board[S * 6 + Y - 1] += 1
print(sum([((i - 1) // K) + 1 for i in board]))