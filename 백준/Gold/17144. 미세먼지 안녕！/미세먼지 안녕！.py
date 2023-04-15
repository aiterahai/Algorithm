"""
file name: 17144.py

create time: 2023-04-13 11:45
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

R, C, T = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(R)]
cleaner = [[x, y] for x in range(R) for y in range(C) if board[x][y] == -1]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

for _ in range(T):

    dusts = [[x, y] for x in range(R) for y in range(C) if board[x][y] > 0]
    changes = []
    for x, y in dusts:
        count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
            if board[nx][ny] == -1: continue
            changes.append([[nx, ny], board[x][y] // 5])
            count += 1
        changes.append([[x, y], -(board[x][y] // 5) * count])

    for edge, value in changes:
        x, y = edge
        board[x][y] += value

    d, x, y = 0, *cleaner[0]
    x, y = x + dx[d], y + dy[d]
    board[x][y] = 0
    while x != cleaner[0][0] or y != cleaner[0][1]:
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx > cleaner[0][0] or ny < 0 or ny >= C: d += 1
        else:
            if board[nx][ny] == -1: break
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            x, y = nx, ny

    d, x, y = 2, *cleaner[1]
    x, y = x + dx[d], y + dy[d]
    while x != cleaner[1][0] or y != cleaner[1][1]:
        board[x][y] = 0
        nx, ny = x + dx[d], y + dy[d]
        if nx < cleaner[1][0] or nx >= R or ny < 0 or ny >= C:
            d += -1
        else:
            if board[nx][ny] == -1: break
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            x, y = nx, ny

print(sum(map(sum, board)) + 2)