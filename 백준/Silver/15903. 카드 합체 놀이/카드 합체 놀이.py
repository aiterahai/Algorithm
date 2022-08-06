from sys import stdin
import heapq

N, M = map(int, stdin.readline().split())
board = list(map(int, stdin.readline().split()))
heapq.heapify(board)
for i in range(M):
    A, B = heapq.heappop(board), heapq.heappop(board)
    heapq.heappush(board, A + B)
    heapq.heappush(board, A + B)
print(sum(board))