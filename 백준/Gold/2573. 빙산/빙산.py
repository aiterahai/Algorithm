"""
file name: 2573.py

create time: 2023-04-13 18:28
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

time = 0
while max(map(max, board)):
    Q = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                Q.append([i, j])
                break
        if Q: break

    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit[Q[-1][0]][Q[-1][1]] = 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if visit[nx][ny] or not board[nx][ny]: continue
            Q.append([nx, ny])
            visit[nx][ny] = 1

    for i in range(N):
        for j in range(M):
            if board[i][j] and not visit[i][j]:
                print(time)
                exit(0)

    minus = []
    for x in range(N):
        for y in range(M):
            if not board[x][y]: continue
            count = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                if board[nx][ny]: continue
                count += 1
            minus.append([x, y, count])

    for x, y, w in minus:
        board[x][y] = max(board[x][y] - w, 0)

    time += 1
print(0)