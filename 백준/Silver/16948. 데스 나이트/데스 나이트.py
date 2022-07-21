from sys import stdin
from collections import deque

N = int(stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]
dx, dy = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]
x, y, r, c = map(int, stdin.readline().split())
board[x][y] = 1
Q = deque([[x, y]])
while Q:
    x, y = Q.popleft()
    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if board[nx][ny]: continue
        board[nx][ny] = board[x][y] + 1
        Q.append([nx, ny])
if board[r][c]: print(board[r][c] - 1)
else: print(-1)