import heapq
from sys import stdin

INF = int(1e9)
N, E = map(int, stdin.readline().split())
graph = [[] for i in range(N + 1)]
for i in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(start, end):
    heap = []
    board = [INF for i in range(N + 1)]
    board[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        weight, node = heapq.heappop(heap)
        if weight > board[node]: continue
        for w, next_node in graph[node]:
            if w + weight < board[next_node]:
                board[next_node] = w + weight
                heapq.heappush(heap, (w + weight, next_node))
    return board[end]

routes = list(map(int, stdin.readline().split()))
result = min(dijkstra(1, routes[0]) + dijkstra(routes[0], routes[1]) + dijkstra(routes[1], N),
             dijkstra(1, routes[1]) + dijkstra(routes[1], routes[0]) + dijkstra(routes[0], N))
print("-1" if result >= INF else result)