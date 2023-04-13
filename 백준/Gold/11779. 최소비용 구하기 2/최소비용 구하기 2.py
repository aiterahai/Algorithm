"""
file name: 11779.py

create time: 2023-04-12 19:25
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
import heapq

def dijkstra(start):
    distance[start] = 0
    Q = []
    heapq.heappush(Q, [start, distance[start]])

    while Q:
        node, wei = heapq.heappop(Q)
        if distance[node] < wei: continue
        for next, next_wei in edges[node]:
            distance_sum = wei + next_wei
            if distance_sum < distance[next]:
                path[next] = node
                distance[next] = distance_sum
                heapq.heappush(Q, [next, distance_sum])

N = int(stdin.readline())
M = int(stdin.readline())
edges = [[] for _ in range(1001)]
distance = [int(1e9) for _ in range(1001)]
path = [0 for _ in range(1001)]
for _ in range(M):
    S, E, W = map(int, stdin.readline().split())
    edges[S].append([E, W])

start, end = map(int, stdin.readline().split())

dijkstra(start)
node = end
result = []
while node:
    result.append(node)
    node = path[node]

print(distance[end])
print(len(result))
print(*result[::-1])