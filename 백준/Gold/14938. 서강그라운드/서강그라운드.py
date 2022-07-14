from sys import stdin
import heapq

INF = int(1e9)
n, m, r = map(int, stdin.readline().split())
items = list(map(int, stdin.readline().split()))
board = [[INF for i in range(n)] for j in range(n)]
for _ in range(r):
    a, b, l = map(int, stdin.readline().split())
    board[a-1][b-1] = l
    board[b-1][a-1] = l
for i in range(n): board[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])
result = 0
for i in board:
    total = 0
    for j, k in enumerate(i):
        if k <= m: total += items[j]
    result = max(result, total)
print(result)