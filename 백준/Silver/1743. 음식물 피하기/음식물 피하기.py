from sys import stdin
from collections import deque

N, M, K = map(int, stdin.readline().split())
board = [[0 for i in range(M)] for j in range(N)]
visit = [[0 for i in range(M)] for j in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(K):
    x, y = map(int, stdin.readline().split())
    board[x-1][y-1] = 1
Q = deque()
result = 0
for i in range(N):
    for j in range(M):
        if not board[i][j] or visit[i][j]: continue
        visit[i][j] = 1
        Q.append([i, j])
        count = 1
        while Q:
            x, y = Q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                if not board[nx][ny] or visit[nx][ny]: continue
                count += 1
                visit[nx][ny] = True
                Q.append([nx, ny])
        result = max(result, count)
print(result)