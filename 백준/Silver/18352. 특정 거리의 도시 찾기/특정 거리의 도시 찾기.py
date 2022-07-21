from sys import stdin
from collections import deque

N, M, K, X = map(int, stdin.readline().split())
graph = [[] for i in range(N + 1)]
visit = [0 for i in range(N + 1)]
for _ in range(M):
    A, B = map(int, stdin.readline().split())
    graph[A].append(B)
Q = deque([X])
visit[X] = 1
while Q:
    node = Q.popleft()
    for i in graph[node]:
        if visit[i]: continue
        visit[i] = visit[node] + 1
        Q.append(i)
if not len([i for i in range(1, N + 1) if visit[i] == K + 1]): print(-1)
for i in [i for i in range(1, N + 1) if visit[i] == K + 1]: print(i)