from sys import stdin

answer = 0
def dfs(node):
    global answer
    if len(graph[node]) == 0 or (len(graph[node]) == 1 and graph[node][0] == M): answer += 1; return
    for i in graph[node]:
        if i == M: continue
        dfs(i)

N = int(stdin.readline())
graph = [[] for i in range(N)]
board = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
for i in range(N):
    if board[i] == -1 or board[i] == M or i == M: continue
    graph[board[i]].append(i)
dfs(board.index(-1))
print(answer if M != board.index(-1) else 0)