from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def dfs(start):
    for i in board[start]:
        if visit[i]: continue
        visit[i] = start
        dfs(i)

N = int(stdin.readline())
board = [[] for i in range(100001)]
for i in range(N-1):
    a, b = map(int, stdin.readline().split())
    board[a].append(b)
    board[b].append(a)

visit = [0] * (N + 1)
visit[1] = 1
dfs(1)
for i in visit[2:]: print(i)