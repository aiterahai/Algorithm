from sys import stdin
from collections import deque

N = int(stdin.readline())
visit = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
for _ in range(int(stdin.readline())):
    A, B = map(int, stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)
Q = deque([1])
visit[1] = 1
while Q:
    node = Q.popleft()
    for i in graph[node]:
        if visit[i]: continue
        visit[i] = visit[node] + 1
        Q.append(i)
print(sum([1 for i in visit if 0 < i <= 3]) - 1)