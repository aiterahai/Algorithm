from sys import stdin
import heapq

INF = int(1e9)
N, M = map(int, stdin.readline().split())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
walls = [stdin.readline().rstrip() for i in range(M)]
board = [[INF for i in range(N)] for j in range(M)]
heap = []

heapq.heappush(heap, (0, 0))
board[0][0] = 0

while heap:
    x, y = heapq.heappop(heap)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
        if board[x][y] + int(walls[nx][ny]) < board[nx][ny]:
            board[nx][ny] = board[x][y] + int(walls[nx][ny])
            heapq.heappush(heap, (nx, ny))

print(board[M-1][N-1])