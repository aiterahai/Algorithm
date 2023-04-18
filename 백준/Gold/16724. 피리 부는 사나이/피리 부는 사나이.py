"""
file name: 16724.py

create time: 2023-04-18 09:46
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

d = dict()
d['D'] = [1, 0]
d['L'] = [0, -1]
d['R'] = [0, 1]
d['U'] = [-1, 0]

N, M = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(N)]
visit = [[-1 for _ in range(M)] for _ in range(N)]

def dfs(x, y, c):
    global answer
    if visit[x][y] != -1:
        if visit[x][y] == c: answer += 1
        return

    visit[x][y] = c
    dfs(x + d[board[x][y]][0], y + d[board[x][y]][1], c)

c = 0
answer = 0
for i in range(N):
    for j in range(M):
        dfs(i, j, c)
        c += 1

print(answer)