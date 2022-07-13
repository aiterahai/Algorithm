import heapq
from sys import stdin
INF = int(1e9)
board = [INF for _ in range(200001)]
N, K = map(int, stdin.readline().split())
heap = []
board[N] = 0
heapq.heappush(heap, (0, N))
while heap:
    weight, node = heapq.heappop(heap)
    for next_node, w in [[node + 1, weight + 1], [node - 1, weight + 1], [node * 2, weight]]:
        if next_node < 0 or next_node > 200000: continue
        if w < board[next_node]:
            board[next_node] = w
            heapq.heappush(heap, (w, next_node))
print(board[K])