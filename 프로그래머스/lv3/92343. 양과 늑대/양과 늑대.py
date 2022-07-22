answer = 0
def dfs(sheep, wolf, info, graph, visit, node):
    global answer
    if info[node] == 1: wolf += 1
    else: sheep += 1
    if sheep <= wolf: return 0
    answer = max(answer, sheep)
    for i in [i for i in range(len(info)) if visit[i]]:
        for j in graph[i]:
            if visit[j]: continue
            visit[j] = 1
            answer = max(answer, dfs(sheep, wolf, info, graph, visit, j))
            visit[j] = 0
    return answer
def solution(info, edges):
    graph = [[] for i in range(len(info))]
    for i, j in edges: graph[i].append(j)
    return dfs(0, 0, info, graph, [1] + [0 for i in range(len(info) - 1)], 0)