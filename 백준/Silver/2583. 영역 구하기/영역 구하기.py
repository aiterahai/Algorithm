from sys import stdin
from collections import deque

m, n, k = map(int, stdin.readline().split())
visit = [[0 for i in range(n)] for j in range(m)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
Q = deque()
result = []
for _ in range(k):
    index = list(map(int, stdin.readline().split()))
    for i in range(index[1], index[3]):
        for j in range(index[0], index[2]):
            visit[i][j] = 1
for _ in range(m):
    for __ in range(n):
        if visit[_][__] == 0:
            Q.append([_, __])
            visit[_][__] = 1
            count = 1
            while Q:
                x, y = Q.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                    if visit[nx][ny] != 0: continue
                    Q.append([nx, ny])
                    visit[nx][ny] = 1
                    count += 1
            result.append(count)
print(len(result))
print(" ".join(map(str, sorted(result))))