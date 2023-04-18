"""
file name: 20040.py

create time: 2023-04-18 10:36
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(M)]
parent = list(range(1000001))

count = 1
for a, b in board:
    if find(a) != find(b):
        union(a, b)
    else:
        print(count)
        exit(0)
    count += 1
print(0)