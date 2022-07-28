from sys import stdin
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for i in range(N)]
visit = [[-1 for i in range(M)] for j in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 2: Q = deque([[i, j]]); visit[i][j] = 0
while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if board[nx][ny] == 0 or visit[nx][ny] != -1: continue
        visit[nx][ny] = visit[x][y] + 1
        Q.append([nx, ny])
for i in range(N):
    for j in range(M):
        print(visit[i][j] if visit[i][j] != -1 else (-1 if visit[i][j] == -1 and board[i][j] == 1 else 0), end=" ")
    print()