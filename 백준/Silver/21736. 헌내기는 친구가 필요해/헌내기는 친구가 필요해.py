from sys import stdin
from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
N, M = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

Q = deque([[i, j] for i in range(N) for j in range(M) if board[i][j] == "I"])

while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if board[nx][ny] == "X" or visit[nx][ny]: continue
        visit[nx][ny] = True
        Q.append([nx, ny])

result = len([1 for i in range(N) for j in range(M) if visit[i][j] and board[i][j] == "P"])
if result: print(result)
else: print("TT")