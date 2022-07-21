from sys import stdin
import heapq

def dijkstra():
    heap = [(0, 0)]
    visit[0][0] = 0
    while heap:
        x, y = heapq.heappop(heap)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            temp = 0
            if board[nx][ny] == "0": temp = 1
            if visit[nx][ny] > visit[x][y] + temp:
                visit[nx][ny] = visit[x][y] + temp
                heapq.heappush(heap, (nx, ny))
INF = int(1e9)
N = int(stdin.readline())
board = [list(stdin.readline()[:-1]) for i in range(N)]
visit = [[INF for i in range(N)] for j in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
dijkstra()
print(visit[N-1][N-1])