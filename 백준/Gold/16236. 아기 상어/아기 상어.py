"""
file name: 16236.py

create time: 2023-04-06 22:01
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
from collections import deque

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
size = 2
count = 0
distance = 0

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

Q = deque([[i, j] for i in range(N) for j in range(N) if board[i][j] == 9])

while True:
    if count == size:
        size += 1
        count = 0
    visit = [[0 for _ in range(N)] for _ in range(N)]
    eatable = []
    eatable_idx = []
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if board[nx][ny] > size or visit[nx][ny]: continue
            visit[nx][ny] = visit[x][y] + 1
            Q.append([nx, ny])
            if board[nx][ny] < size and 0 < board[nx][ny] < 9:
                eatable.append([nx, ny])
                eatable_idx.append(visit[nx][ny])
    if not eatable: break
    min_distance = min(eatable_idx)
    possible = sorted([i for i, j in zip(eatable, eatable_idx) if j == min_distance], key=lambda x : (x[0], x[1]))
    x, y = possible[0]
    Q.append([x, y])
    distance += visit[x][y]
    for i, j in [[i, j] for i in range(N) for j in range(N) if board[i][j] == 9]:
        board[i][j] = 0
    board[x][y] = 9
    count += 1
print(distance)