from sys import stdin

for _ in range(int(stdin.readline())):
    INF = int(1e9)
    N, M = map(int, stdin.readline().split())
    graph = [[INF for _ in range(N)] for _ in range(N)]
    for i in range(N): graph[i][i] = 0
    for _ in range(M):
        A, B, C = map(int, stdin.readline().split())
        graph[A-1][B-1], graph[B-1][A-1] = C, C
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    K = int(stdin.readline())
    friend = list(map(int, stdin.readline().split()))
    result = [0 for i in range(N)]
    for i in range(N):
        for j in friend:
            result[i] += graph[j-1][i]
    print(result.index(min(result))+1)