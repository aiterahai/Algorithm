from sys import stdin
from collections import deque

def bfs(start):
    Q = deque()
    Q.append(start)
    visit[start][start] = 1
    while Q:
        node = Q.popleft()
        for i in board[node]:
            if visit[start][i]: continue
            visit[start][i] = visit[start][node] + 1
            Q.append(i)

N, M = map(int, stdin.readline().split())
board = [[] for i in range(N + 1)]
visit = [[0 for i in range(N + 1)] for j in range(N + 1)]

for i in range(M):
    a, b = map(int, stdin.readline().split())
    board[a].append(b)
    board[b].append(a)
for i in range(1, N + 1):
    board[i].sort()
for i in range(1, N + 1):
    bfs(i)
sum_p = min(list(map(sum, visit))[1:])
print(list(map(sum, visit)).index(sum_p))