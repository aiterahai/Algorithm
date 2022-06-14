from sys import stdin
from collections import deque
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n = int(stdin.readline())
paint = [list(stdin.readline()) for i in range(n)]
b_paint = paint
Q = deque()
visit = [[False for i in range(n)] for j in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if visit[i][j]: continue
        Q.append([i, j])
        visit[i][j] = True
        while Q:
            x, y = Q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if visit[nx][ny] == True or paint[x][y] != paint[nx][ny]: continue
                Q.append([nx, ny])
                visit[nx][ny] = True
        count += 1
print(count)

b_visit = [[False for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if b_paint[i][j] == "R":
            b_paint[i][j] = "G"

count = 0
for i in range(n):
    for j in range(n):
        if b_visit[i][j] == True: continue
        Q.append([i, j])
        b_visit[i][j] = True
        while Q:
            x, y = Q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if b_visit[nx][ny] == True or b_paint[x][y] != b_paint[nx][ny]: continue
                Q.append([nx, ny])
                b_visit[nx][ny] = True
        count += 1
print(count)