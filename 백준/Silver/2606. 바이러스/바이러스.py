from sys import stdin
from collections import deque

N = int(stdin.readline())
board = [[0 for i in range(N)] for j in range(N)]
visit = [[0 for i in range(N)] for j in range(N)]
for i in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    board[n-1][m-1] = 1
    board[m-1][n-1] = 1

Q = deque([0])
while Q:
    x = Q.popleft()
    for i in range(N):
        if board[x][i] and not visit[x][i]:
            Q.append(i)
            visit[x][i] = 1
print(sum(map(max, visit)) - 1)