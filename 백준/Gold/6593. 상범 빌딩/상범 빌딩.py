from sys import stdin
from collections import deque

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
while True:
    L, R, C = map(int, stdin.readline().split())
    if not L and not R and not C: break
    board = []
    visit = [[[0 for i in range(C)] for j in range(R)] for k in range(L)]
    Q = deque()
    for i in range(L):
        board_ = [stdin.readline().strip() for i in range(R)]
        board.append(board_)
        input()
    break_point = False
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if board[i][j][k] == "S":
                    Q.append([i, j, k])
                    visit[i][j][k] = 1
                if board[i][j][k] == "E":
                    x_, y_, z_ = i, j, k

    exited = False
    while Q:
        x, y, z = Q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if nx < 0 or nx >= L or ny < 0 or ny >= R or nz < 0 or nz >= C: continue
            if visit[nx][ny][nz] or board[nx][ny][nz] == "#": continue
            Q.append([nx, ny, nz])
            visit[nx][ny][nz] = visit[x][y][z] + 1
            if board[nx][ny][nz] == "E":
                exited = True
                break
    if exited: print("Escaped in", visit[x_][y_][z_] - 1, "minute(s).")
    else: print("Trapped!")