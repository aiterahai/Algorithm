from sys import stdin

V, S = map(int, stdin.readline().split())
node = []
for _ in range(S):
    a, b, w = map(int, stdin.readline().split())
    node.append((w, a, b))
node.sort(key=lambda x: x[0])

parent = list(range(V + 1))

def union(a, b):
    a, b = find(a), find(b)

    if b < a: parent[a] = b
    else: parent[b] = a


def find(a):
    if a == parent[a]: return a
    parent[a] = find(parent[a])
    return parent[a]

result = 0
for w, s, e in node:
    if find(s) != find(e):
        union(s, e)
        result += w
print(result)