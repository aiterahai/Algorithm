from collections import deque
from sys import stdin

m, n = map(int, stdin.readline().split())
farm = [list(map(int, stdin.readline().split())) for i in range(n)]
day = [[0 for i in range(m)] for j in range(n)]
Q = deque()
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        if farm[i][j] == 1:
            day[i][j] = 1
            Q.append([i, j])
max_x, max_y = 0, 0
while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if day[nx][ny] != 0 or farm[nx][ny] == -1 or farm[nx][ny] == 1: continue
        Q.append([nx, ny])
        day[nx][ny] = day[x][y] + 1
        max_x, max_y = nx, ny
for i in range(n):
    for j in range(m):
        if farm[i][j] == 0 and day[i][j] == 0:
            print(-1)
            exit(0)
print(day[max_x][max_y] - 1)