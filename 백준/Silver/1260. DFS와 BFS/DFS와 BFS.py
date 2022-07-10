from collections import deque
from sys import stdin

N, M, V = map(int, stdin.readline().split())
board = [[] for i in range(N + 1)]
visit = [0 for i in range(N + 1)]

for i in range(M):
    a, b = map(int, stdin.readline().split())
    board[a].append(b)
    board[b].append(a)
for i in range(N + 1):
    board[i] = sorted(board[i])

visit[V] = 1
def dfs(i):
    print(i, end=" ")
    for j in board[i]:
        if visit[j]: continue
        visit[j] = 1
        dfs(j)
dfs(V)
print()
Q = deque([V])
print(V, end=" ")

visit = [0 for i in range(N + 1)]
visit[V] = 1
while Q:
    x = Q.popleft()
    for i in board[x]:
        if visit[i]: continue
        Q.append(i)
        visit[i] = 1
        print(i, end=" ")