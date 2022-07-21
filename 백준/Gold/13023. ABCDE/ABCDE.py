from sys import stdin

def dfs(node, K):
    if K == 4: print(1); exit(0)
    for i in board[node]:
        if i in visit: continue
        visit.append(i)
        dfs(i, K + 1)
        visit.pop()

N, M = map(int, stdin.readline().split())
board = [[] for i in range(N)]
visit = []
for i in range(M):
    a, b = map(int, stdin.readline().split())
    board[a].append(b)
    board[b].append(a)
for i in range(N):
    visit.append(i)
    dfs(i, 0)
    visit.pop()
print(0)