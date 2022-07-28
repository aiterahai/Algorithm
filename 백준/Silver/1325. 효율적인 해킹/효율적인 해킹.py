from sys import stdin
from collections import deque

def bfs(node):
    visit = [0 for i in range(N + 1)]
    visit[node], count = 1, 1
    Q = deque([node])
    while Q:
        node = Q.popleft()
        for i in graph[node]:
            if visit[i]: continue
            visit[i], count = 1, count + 1
            Q.append(i)
    return count

N, M = map(int, stdin.readline().split())
graph = [[] for i in range(N + 1)]
for _ in range(M):
    A, B = map(int, stdin.readline().split())
    graph[B].append(A)

result = [bfs(i) for i in range(1, N + 1)]
temp = max(result)
print(*[i + 1 for i in range(N) if result[i] == temp])