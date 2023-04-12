"""
file name: 1865.py

create time: 2023-04-12 12:05
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
INF = int(1e9)

def bf(start):
    distance[start] = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for next, time in edges[j]:
                if distance[next] > distance[j] + time:
                    distance[next] = distance[j] + time
                    if i == N:
                        return True

    return False

for _ in range(int(stdin.readline())):
    N, M, W = map(int, stdin.readline().split())

    edges = [[] for _ in range(N + 1)]
    distance = [INF for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, stdin.readline().split())
        edges[S].append([E, T])
        edges[E].append([S, T])

    for _ in range(W):
        S, E, T = map(int, stdin.readline().split())
        edges[S].append([E, -T])

    if bf(1): print("YES")
    else: print("NO")