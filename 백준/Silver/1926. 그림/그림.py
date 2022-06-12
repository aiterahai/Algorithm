from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for i in range(n)]
visit = [[False for i in range(m)] for j in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Q = deque()
count = 0
max = -999999

for i in range(n):
    for j in range(m):
        size = 0
        if visit[i][j] == True or board[i][j] == 0: continue
        count += 1
        length = 1
        Q.append([i, j])
        visit[i][j] = True
        while length:
            size += 1
            x, y = Q.popleft()
            length -= 1
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if (nx < 0 or nx >= n or ny < 0 or ny >= m): continue
                if (visit[nx][ny] or board[nx][ny] == 0): continue
                Q.append([nx, ny])
                length += 1
                visit[nx][ny] = True
        if(size > max): max = size
print(count)
if(max < 0): print(0)
else: print(max)