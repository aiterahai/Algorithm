from collections import deque
from sys import stdin

r, c = map(int, stdin.readline().split())
maze = [stdin.readline() for i in range(r)]
fire = [[9999999 for i in range(c)] for j in range(r)]
time = [[0 for i in range(c)] for j in range(r)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
Q = deque()

for i in range(r):
    for j in range(c):
        if maze[i][j] == "F":
            fire[i][j] = 0
            Q.append([i, j])

while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
        if maze[nx][ny] == "#" or fire[nx][ny] != 9999999: continue
        Q.append([nx, ny])
        fire[nx][ny] = fire[x][y] + 1
for i in range(r):
    for j in range(c):
        if maze[i][j] == "J":
            time[i][j] = 1
            Q.append([i, j])
while Q:
    x, y = Q.popleft()
    if x == r-1 or y == c-1 or x == 0 or y == 0:
        print(time[x][y])
        exit(0)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
        if maze[nx][ny] == "#" or fire[nx][ny] <= time[x][y] or time[nx][ny] != 0: continue
        Q.append([nx, ny])
        time[nx][ny] = time[x][y] + 1
print("IMPOSSIBLE")