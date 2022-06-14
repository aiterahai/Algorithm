from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())
storage = [[list(map(int, stdin.readline().split())) for i in range(n)] for j in range(h)]
visit = [[[0 for i in range(m)] for j in range(n)] for k in range(h)]
dx, dy, dz = [0, 0, 1, 0, 0, -1], [0, 1, 0, 0, -1, 0], [1, 0, 0, -1, 0, 0]
Q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if storage[i][j][k] == 0 or storage[i][j][k] == -1: continue
            Q.append([i, j, k])
            visit[i][j][k] = 1
max_value = 1
while Q:
    x, y, z = Q.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m: continue
        if visit[nx][ny][nz] != 0 or storage[nx][ny][nz] == -1: continue
        Q.append([nx, ny, nz])
        visit[nx][ny][nz] = visit[x][y][z] + 1
        max_value = visit[nx][ny][nz]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if visit[i][j][k] == 0 and storage[i][j][k] == 0:
                print(-1)
                exit(0)
print(max_value-1)