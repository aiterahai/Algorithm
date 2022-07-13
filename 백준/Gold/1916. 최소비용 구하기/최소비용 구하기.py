from sys import stdin
import heapq

INF = int(1e9)
N = int(stdin.readline())
M = int(stdin.readline())
graph = [[] for i in range(N + 1)]
board = [INF for i in range(N + 1)]
heap = []

for _ in range(M):
    a, b, p = map(int, stdin.readline().split())
    graph[a].append((p, b))

START, END = map(int, stdin.readline().split())
board[START] = 0
heapq.heappush(heap, (0, START))

while heap:
    weight, node = heapq.heappop(heap)
    if board[node] < weight: continue
    for w, next_node in graph[node]:
        if w + weight < board[next_node]:
            board[next_node] = w + weight
            heapq.heappush(heap, (w + weight, next_node))

print(board[END])