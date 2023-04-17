from sys import stdin


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, stdin.readline().split())
edges = []
for _ in range(M):
    A, B, C = map(int, stdin.readline().split())
    edges.append([C, A, B])

parent = [i for i in range(N + 1)]

edges = sorted(edges)

last = 0
answer = 0
for C, A, B in edges:
    if find(A) != find(B):
        union(A, B)
        answer += C
        last = C

answer -= last
print(answer)