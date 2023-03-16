from sys import stdin

N, M = map(int, stdin.readline().split())
x, y, d = map(int, stdin.readline().split())
result = 0

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

board = [list(map(int, stdin.readline().split())) for _ in range(N)]

while True:
    if board[x][y] == 0:
        board[x][y] = 2
        result += 1
    if sum([1 for i in range(4) if board[x + dx[i]][y + dy[i]] == 0]) == 0:
        nx, ny = x - dx[d], y - dy[d]
        if board[nx][ny] == 1: break
        x, y = nx, ny
        continue
    while True:
        d = (d + 3) % 4
        nx, ny = x + dx[d], y + dy[d]
        if board[nx][ny] == 0: break
    x, y = nx, ny

print(sum([i.count(2) for i in board]))