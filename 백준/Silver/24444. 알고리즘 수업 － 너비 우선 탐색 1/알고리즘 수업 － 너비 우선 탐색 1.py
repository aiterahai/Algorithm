from sys import stdin
from collections import deque

N, M, R = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)
for i in range(1, N + 1): graph[i].sort()
Q = deque([R])
count = 1
visit[R] = count
while Q:
    node = Q.popleft()
    for i in graph[node]:
        if visit[i]: continue
        count += 1
        visit[i] = count
        Q.append(i)
print(*visit[1:], sep="\n")