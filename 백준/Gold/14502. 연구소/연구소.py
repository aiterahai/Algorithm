"""
file name: 14502.py

create time: 2023-04-12 18:07
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from itertools import combinations
from collections import deque
from sys import stdin

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs():
    visit = [[0 for _ in range(M)] for _ in range(N)]
    virus = [[i, j] for i in range(N) for j in range(M) if board[i][j] == 2]
    Q = deque(virus)
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if board[nx][ny] or visit[nx][ny]: continue
            visit[nx][ny] = 1
            Q.append([nx, ny])

    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 and not visit[i][j]: count += 1

    return count

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
empty = [[i, j] for i in range(N) for j in range(M) if not board[i][j]]
walls = list(combinations(empty, 3))

result = 0
for i in range(len(walls)):
    for x, y in walls[i]: board[x][y] = 1
    result = max(result, bfs())
    for x, y in walls[i]: board[x][y] = 0

print(result)