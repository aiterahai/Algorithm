from sys import stdin
import heapq

INF = int(1e9)
def dijkstra(start):
    heap = [(0, start)]
    visit[start] = 0
    while heap:
        w, node = heapq.heappop(heap)
        for next_node, weight in graph[node]:
            if visit[next_node] > weight + w:
                visit[next_node] = weight + w
                heapq.heappush(heap, (visit[next_node], next_node))

for _ in range(int(stdin.readline())):
    N, D, C = map(int, stdin.readline().split())
    graph = [[] for i in range(N+1)]
    visit = [INF for i in range(N+1)]
    for __ in range(D):
        a, b, s = map(int, stdin.readline().split())
        graph[b].append([a, s])
    dijkstra(C)
    print(len([i for i in visit if i != INF]), max([i for i in visit if i != INF]))