from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
indegree = [0 for i in range(N + 1)]
board = [[] for i in range(N + 1)]
for i in range(M):
    A, B = map(int, stdin.readline().split())
    board[A].append(B)
    indegree[B] += 1
Q = deque([i for i in range(1, N + 1) if indegree[i] == 0])
while Q:
    node = Q.popleft()
    print(node, end=" ")
    for i in board[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            Q.append(i)