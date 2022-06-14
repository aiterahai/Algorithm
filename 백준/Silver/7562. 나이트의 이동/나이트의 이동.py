from sys import stdin
from collections import deque

dx, dy = [1, 2, 2, 1, -1, -1, -2, -2], [2, 1, -1, -2, 2, -2, 1, -1]
t = int(stdin.readline())
for _ in range(t):
    Q = deque()
    length = int(stdin.readline())
    board = [[0 for i in range(length)] for j in range(length)]
    start_index = list(map(int, stdin.readline().split()))
    end_index = list(map(int, stdin.readline().split()))
    Q.append(start_index)
    board[start_index[0]][start_index[1]] = 1
    while Q:
        x, y = Q.popleft()
        if x == end_index[0] and y == end_index[1]:
            print(board[x][y]-1)
            break
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= length or ny < 0 or ny >= length: continue
            if board[nx][ny] != 0: continue
            Q.append([nx, ny])
            board[nx][ny] = board[x][y] + 1