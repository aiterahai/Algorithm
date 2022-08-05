from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
count = 1
def dfs(R):
    global count
    for node in sorted(graph[R], reverse=True):
        if visit[node]: continue
        count += 1
        visit[node] = count
        dfs(node)

N, M, R = map(int, stdin.readline().split())
graph = [[] for i in range(N + 1)]
for _ in range(M):
    A, B = map(int, stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)
visit = [0] * (N + 1)
visit[R] = count
dfs(R)
print(*visit[1:], sep="\n")