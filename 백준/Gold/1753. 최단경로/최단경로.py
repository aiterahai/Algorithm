from sys import stdin
import heapq

INF = int(1e9)
V, E = map(int, stdin.readline().split())
K = int(stdin.readline())
heap = []
graph = [[] for i in range(V + 1)]
board = [INF for i in range(V + 1)]
for i in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((w, v))

board[K] = 0
heapq.heappush(heap, (0, K))

while heap:
    weight, node = heapq.heappop(heap)

    if board[node] < weight: continue
    for w, next_node in graph[node]:
        if weight + w < board[next_node]:
            board[next_node] = weight + w
            heapq.heappush(heap, (weight + w, next_node))

for i in board[1:]: print("INF" if i == INF else i)