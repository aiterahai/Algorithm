M, N = map(int, input().split())
board = sorted(map(int, input().split()))
visit = []


def dfs(K):
    if K == N: print(" ".join(map(str, visit))); return
    for i in range(M):
        if K == 0 or visit[K - 1] <= board[i]:
            visit.append(board[i])
            dfs(K + 1)
            visit.pop()

dfs(0)