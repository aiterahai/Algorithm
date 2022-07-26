from sys import stdin
from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
result = 0
def bfs(x, y):
    global result
    Q = deque([(x, y)])
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= L or ny < 0 or ny >= W: continue
            if board[nx][ny] == "W" or visit[nx][ny]: continue
            visit[nx][ny] = visit[x][y] + 1
            Q.append((nx, ny))
    result = max(result, max(map(max, visit)))

L, W = map(int, stdin.readline().split())
board = [stdin.readline()[:-1] for i in range(L)]
visit = [[0 for i in range(W)] for i in range(L)]
for i in range(L):
    for j in range(W):
        if board[i][j] == "L":
            visit[i][j] = 1
            bfs(i, j)
            visit = [[0 for _ in range(W)] for _ in range(L)]
print(result-1)