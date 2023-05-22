from sys import stdin
from collections import deque

N, Q = map(int, stdin.readline().split())
edges = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, stdin.readline().split())
    edges[p].append([q, r])
    edges[q].append([p, r])

for _ in range(Q):
    k, v = map(int, stdin.readline().split())

    visit = [False for _ in range(N + 1)]
    visit[v] = True
    result = 0
    Q = deque([(v, float('inf'))])

    while Q:
        v, usado = Q.pop()
        for next_v, next_usado in edges[v]:
            next_usado = min(usado, next_usado)
            if not visit[next_v] and next_usado >= k:
                result += 1
                Q.append((next_v, next_usado))
                visit[next_v] = True

    print(result)