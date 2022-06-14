from sys import stdin
from collections import deque
f, s, g, u, d = map(int, stdin.readline().split())
dx = [u, -1*d]
visit = [0 for i in range(1000001)]
Q = deque()
visit[s] = 1
Q.append(s)
if s == g:
    print(0)
    exit(0)
while Q:
    x = Q.popleft()
    for i in range(2):
        nx = x + dx[i]
        if nx <= 0 or nx > f: continue
        if visit[nx] != 0: continue
        Q.append(nx)
        visit[nx] = visit[x] + 1
        if nx == g:
            print(visit[x])
            exit(0)
print("use the stairs")