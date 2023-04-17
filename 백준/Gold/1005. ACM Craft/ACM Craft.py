"""
file name: 1005.py

create time: 2023-04-17 22:52
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
from collections import deque

for _ in range(int(stdin.readline())):
    N, K = map(int, stdin.readline().split())
    board = [0] + list(map(int, stdin.readline().split()))
    edges = [[] for _ in range(N + 1)]
    inDegree = [0 for _ in range(N + 1)]
    table = [0 for _ in range(N + 1)]

    for _ in range(K):
        X, Y = map(int, stdin.readline().split())
        edges[X].append(Y)
        inDegree[Y] += 1

    Q = deque()
    for i in range(1, N + 1):
        if inDegree[i]: continue
        Q.append(i)
        table[i] = board[i]

    while Q:
        node = Q.popleft()
        for i in edges[node]:
            inDegree[i] -= 1
            table[i] = max(table[node] + board[i], table[i])
            if inDegree[i] == 0:
                Q.append(i)

    print(table[int(stdin.readline())])