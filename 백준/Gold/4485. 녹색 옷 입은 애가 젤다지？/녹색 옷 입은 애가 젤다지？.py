from collections import deque
from sys import stdin
import heapq
INF = int(1e9)

count = 1
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def dijkstra(N, board):
    global count
    visit = [[INF for i in range(N)] for j in range(N)]
    heap = [(board[0][0], 0, 0)]
    visit[0][0] = 0
    while heap:
        weight, x, y = heapq.heappop(heap)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            w = weight + board[nx][ny]
            if w < visit[nx][ny]:
                visit[nx][ny] = w
                heapq.heappush(heap, (w, nx, ny))
    print(f"Problem {count}: {visit[N-1][N-1]}")
    count += 1


while True:
    N = int(stdin.readline())
    if not N: break
    dijkstra(N, [list(map(int, stdin.readline().split())) for _ in range(N)])