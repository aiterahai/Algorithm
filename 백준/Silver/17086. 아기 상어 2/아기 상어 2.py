from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for i in range(N)]
dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0 ,1]
Q = deque([])
for i in range(N):
    for j in range(M):
        if board[i][j]: Q.append([i, j])
while Q:
    x, y = Q.popleft()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if board[nx][ny]: continue
        board[nx][ny] = board[x][y] + 1
        Q.append([nx, ny])
print(max(map(max, board)) - 1)