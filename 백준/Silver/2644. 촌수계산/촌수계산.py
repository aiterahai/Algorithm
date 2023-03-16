from sys import stdin
from collections import deque

N = int(stdin.readline())
A, B = map(int, stdin.readline().split())
board = [[] for _ in range(N + 1)]

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    board[a] += [b]
    board[b] += [a]

visit = [0] * (N + 1)
Q = deque([A])
while Q:
    x = Q.popleft()
    for i in board[x]:
        if visit[i] != 0: continue
        visit[i] = visit[x] + 1
        Q.append(i)
print(visit[B] if visit[B] else -1)