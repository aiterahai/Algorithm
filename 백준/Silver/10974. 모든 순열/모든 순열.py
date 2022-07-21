N = int(input())
visit = []
def dfs(K):
    if K == N: print(*visit)
    else:
        for i in range(1, N + 1):
            if i in visit: continue
            visit.append(i)
            dfs(K + 1)
            visit.pop()
dfs(0)