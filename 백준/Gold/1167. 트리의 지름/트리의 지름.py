"""
file name: 1167.py

create time: 2023-04-12 21:52
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
from collections import deque

V = int(stdin.readline())
edges = [[] for _ in range(V + 1)]

for _ in range(V):
    arr = list(map(int, stdin.readline().split()))
    for i in range(1, len(arr) - 2, 2):
        edges[arr[0]].append([arr[i], arr[i + 1]])

def bfs(start):
    visit = [-1 for _ in range(V + 1)]
    Q = deque([start])
    visit[start] = 0
    while Q:
        node = Q.popleft()
        for next, weight in edges[node]:
            if visit[next] != -1: continue
            visit[next] = visit[node] + weight
            Q.append(next)

    return max(visit), visit.index(max(visit))

value, next = bfs(1)
value, next = bfs(next)
print(value)