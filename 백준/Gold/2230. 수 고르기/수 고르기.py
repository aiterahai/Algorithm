from sys import stdin

N, M = map(int, stdin.readline().split())
board = sorted(int(stdin.readline()) for i in range(N))

result = 999999999999999999999
start, end = 0, 0
while True:
    if end >= N or start >= N: break
    if board[end] - board[start] >= M:
        result = min(board[end] - board[start], result)
        start += 1
    else: end += 1
print(result)