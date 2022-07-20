from sys import stdin
result = 1
def dfs(K, x, y):
    global result
    result = max(result, K)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
        if visit[ord(board[nx][ny]) - 65]: continue
        visit[ord(board[nx][ny]) - 65] = 1
        dfs(K + 1, nx, ny)
        visit[ord(board[nx][ny]) - 65] = 0
R, C = map(int, stdin.readline().split())
board = [stdin.readline().rstrip() for i in range(R)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visit = [0 for i in range(26)]
visit[ord(board[0][0]) - 65] = 1

dfs(1, 0, 0)
print(result)