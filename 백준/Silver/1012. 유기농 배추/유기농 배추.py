from sys import stdin
from collections import deque
t = int(stdin.readline())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(t):
    count = 0
    m, n, k = map(int, stdin.readline().split())
    farm = [[0 for i in range(m)] for j in range(n)]
    Q = deque()
    for j in range(k):
        temp1, temp2 = map(int, stdin.readline().split())
        farm[temp2][temp1] = 1
    for j in range(n):
        for k in range(m):
            if farm[j][k] == 1:
                farm[j][k] = 0
                Q.append([j, k])
                while Q:
                    x, y = Q.popleft()
                    for l in range(4):
                        nx, ny = x + dx[l], y + dy[l]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                        if farm[nx][ny] == 0: continue
                        Q.append([nx, ny])
                        farm[nx][ny] = 0
                count += 1
    print(count)