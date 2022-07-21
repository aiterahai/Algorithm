from sys import stdin

N = int(stdin.readline())
board = list(map(int, stdin.readline().split()))
visit = [0 for i in range(2000001)]

def dfs(idx, M):
    if idx == N: return
    M += board[idx]
    visit[M] = 1
    dfs(idx + 1, M)
    dfs(idx + 1, M - board[idx])

dfs(0, 0)
print(visit[1:].index(0)+1)