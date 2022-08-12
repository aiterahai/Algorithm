from sys import stdin

def dfs(K, value):
    if K == M:
        if value <= N: print(value); exit(0)
        return
    for i in board: dfs(K + 1, value * 10 + i)

N, M = map(int, stdin.readline().split())
M = len(str(N))
board = sorted(list(map(int, stdin.readline().split())))[::-1]
for i in range(0, 10000): dfs(i, 0)