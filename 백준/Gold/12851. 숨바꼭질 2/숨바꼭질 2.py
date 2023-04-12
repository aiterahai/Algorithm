"""
file name: 12851.py

create time: 2023-04-12 18:21
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
from collections import deque

distance = [[0, 1] for _ in range(100001)]

N, K = map(int, stdin.readline().split())
Q = deque([N])
distance[N] = [1, 1]

while Q:
    node = Q.popleft()
    for next in [node + 1, node - 1, node * 2]:
        if next < 0 or next > 100000: continue
        if distance[node][0] + 1 == distance[next][0]: distance[next][1] += distance[node][1]
        if distance[next][0]: continue
        distance[next][0] = distance[node][0] + 1
        distance[next][1] += distance[node][1] - 1
        Q.append(next)

print(distance[K][0] - 1, distance[K][1], sep="\n")