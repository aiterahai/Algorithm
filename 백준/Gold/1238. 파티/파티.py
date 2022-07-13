from sys import stdin
import heapq

INF = int(1e9)
N, M, X = map(int, stdin.readline().split())
graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b, p = map(int, stdin.readline().split())
    graph[a].append((p, b))

def dijkstar(start, end):
    board = [INF for i in range(N + 1)]
    heap = []
    heapq.heappush(heap, (0, start))
    board[start] = 0

    while heap:
        weight, node = heapq.heappop(heap)
        if weight > board[node]: continue
        for w, next_node in graph[node]:
            if w + weight < board[next_node]:
                board[next_node] = w + weight
                heapq.heappush(heap, (w + weight, next_node))

    return board[end]

print(max([dijkstar(i, X) + dijkstar(X, i) for i in range(1, N + 1)]))