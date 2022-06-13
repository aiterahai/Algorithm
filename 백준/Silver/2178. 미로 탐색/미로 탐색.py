from sys import stdin
from queue import Queue

n, m = map(int, stdin.readline().split())
maze = [stdin.readline()[:-1] for i in range(n)]
distance = [[0 for i in range(m)] for j in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
Q = Queue()
Q.put([0, 0])
distance[0][0] = 1
while not Q.empty():
    x, y = Q.get()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if maze[nx][ny] == "0" or distance[nx][ny] != 0: continue
        distance[nx][ny] = distance[x][y] + 1
        Q.put([nx, ny])
print(distance[n-1][m-1])