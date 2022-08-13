from sys import stdin
from collections import deque

dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]
N, M = map(int, stdin.readline().split())
visit = [[-1 for _ in range(N)] for _ in range(N)]
A, B = map(int, stdin.readline().split())
Q = deque([[A-1, B-1]])
visit[A-1][B-1] = 0
while Q:
    x, y = Q.popleft()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if visit[nx][ny] != -1: continue
        visit[nx][ny] = visit[x][y] + 1
        Q.append([nx, ny])
for _ in range(M):
    A, B = map(int, stdin.readline().split())
    print(visit[A-1][B-1], end=" ")