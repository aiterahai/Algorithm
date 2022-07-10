from sys import stdin
from collections import deque

def bfs(start):
    Q = deque([start])
    visit[start] = True
    while Q:
        x = Q.popleft()
        for i in board[x]:
            if visit[i]: continue
            visit[i] = True
            Q.append(i)

N, M = map(int, stdin.readline().split())
board = [[] for i in range(N + 1)]

for i in range(M):
    a, b = map(int, stdin.readline().split())
    board[a].append(b)
    board[b].append(a)

visit = [False for i in range(N + 1)]

count = 0
for i in range(1, N+1):
    if visit[i]: continue
    if not board[i]: count, visit[i] = count + 1, True
    else:
        count = count + 1
        bfs(i)
print(count)