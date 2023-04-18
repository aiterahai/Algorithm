"""
file name: 2636.py

create time: 2023-04-18 14:54
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

result = 0
cheese = 0
while [0 for i in range(N) for j in range(M) if board[i][j] == 1]:
    result += 1
    Q = deque([[i, j] for i in range(N) for j in range(M) if i == 0 or i == N - 1 or j == 0 or j == M - 1])
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if board[nx][ny] != 0: continue
            board[nx][ny] = 2
            Q.append([nx, ny])

    cheese = sum([i.count(1) for i in board])

    for x in range(N):
        for y in range(M):
            if board[x][y] == 1:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                    if board[nx][ny] == 2: board[x][y] = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == 2: board[i][j] = 0

print(result)
print(cheese)