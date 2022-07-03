from sys import stdin
from collections import deque

n = int(stdin.readline())
height = [list(map(int, stdin.readline().split())) for i in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
max_area = 0
for location in range(min(map(min, height)) - 1, max(map(max, height))+1):
    visit = [[False for i in range(n)] for j in range(n)]
    Q = deque()
    count = 0
    for i in range(n):
        for j in range(n):
            if height[i][j] <= location: visit[i][j] = True
    for i in range(n):
        for j in range(n):
            if visit[i][j]: continue
            Q.append([i, j])
            while Q:
                x, y = Q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                    if visit[nx][ny]: continue
                    Q.append([nx, ny])
                    visit[nx][ny] = True
            count += 1
    max_area = max(max_area, count)
print(max_area)