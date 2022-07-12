from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
board = [stdin.readline().rstrip() for i in range(N)]
dx, dy = [1, -1, 0 ,0], [0, 0, 1, -1]
w, b = 0, 0
for i in ["W", "B"]:
    visit = [[0 for j in range(M)] for i in range(N)]
    Q = deque()
    for j in range(N):
        for k in range(M):
            if visit[j][k] or board[j][k] != i: continue
            visit[j][k] = 1
            Q.append([j, k])
            count = 1
            while Q:
                x, y = Q.popleft()
                for l in range(4):
                    nx, ny = dx[l] + x, dy[l] + y
                    if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                    if board[nx][ny] != i or visit[nx][ny]: continue
                    visit[nx][ny] = True
                    Q.append([nx, ny])
                    count += 1
            if i == "W": w += count ** 2
            else: b += count ** 2
print(w, b)