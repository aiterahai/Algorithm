"""
file name: 4386.py

create time: 2023-04-18 08:48
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def distance(x1, x2, y1, y2):
    return ((x1 - y1) ** 2 + (x2 - y2) ** 2) ** 0.5

N = int(stdin.readline())
parent = list(range(N + 1))
stars = [list(map(float, stdin.readline().split())) for _ in range(N)]
edges = sorted([(distance(*stars[i], *stars[j]), i, j) for i in range(N - 1) for j in range(i + 1, N)])

result = 0
for weight, x, y in edges:
    if find(x) == find(y): continue
    union(x, y)
    result += weight

print(round(result, 2))