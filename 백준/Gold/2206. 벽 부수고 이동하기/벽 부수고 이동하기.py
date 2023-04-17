from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
graph = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, stdin.readline()[:-1])))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

x, y, z = 0, 0, 0
queue = deque()
queue.append((x, y, z))

while queue:
    a, b, c = queue.popleft()
    if a == n - 1 and b == m - 1:
        print(visited[a][b][c])
        exit(0)
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1 and c == 0 :
            visited[nx][ny][1] = visited[a][b][0] + 1
            queue.append((nx, ny, 1))
        elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
            visited[nx][ny][c] = visited[a][b][c] + 1
            queue.append((nx, ny, c))
print(-1)
exit(0)