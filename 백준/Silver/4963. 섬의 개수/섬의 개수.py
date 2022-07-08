from sys import stdin
from collections import deque

dx, dy = [-1, 0, 1, -1, 1, -1, 0, 1], [1, 1, 1, 0, 0, -1, -1, -1]
while True:
    w, h = map(int, stdin.readline().split())
    if not w and not h: break
    board = [list(map(int, stdin.readline().split())) for i in range(h)]
    visit = [[False for i in range(w)] for j in range(h)]
    Q = deque()
    count = 0
    for i in range(h):
        for j in range(w):
            if not board[i][j] or visit[i][j]: continue
            Q.append([i, j])
            visit[i][j] = True
            while Q:
                x, y = Q.popleft()
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
                    if visit[nx][ny] or not board[nx][ny]: continue
                    Q.append([nx, ny])
                    visit[nx][ny] = True
            count += 1
    print(count)