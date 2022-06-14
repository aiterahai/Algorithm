from sys import stdin
from collections import deque
n = int(stdin.readline())
visit = [list(stdin.readline()) for i in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
Q = deque()
result = []
for i in range(n):
    for j in range(n):
        if visit[i][j] == "0": continue
        count = 1
        Q.append([i, j])
        visit[i][j] = "0"
        while Q:
            x, y = Q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if visit[nx][ny] == "0": continue
                Q.append([nx, ny])
                count += 1
                visit[nx][ny] = "0"
        result.append(count)
print(len(result))
for i in sorted(result):
    print(i)