from sys import stdin

visit = []
diff = int(1e9)
def value():
    global diff
    start, link = [i for i in range(N) if not visit[i]], [i for i in range(N) if visit[i]]
    diff = min(diff, abs(sum([board[i][j] for i in start for j in start]) - sum([board[i][j] for i in link for j in link])))

def dfs(x, y, K):
    if x > N // 2 or y > N // 2: return
    if K == N: value()
    for i in [0, 1]:
        visit.append(i)
        dfs(x + i, y + abs(i - 1), K + 1)
        visit.pop()


N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for i in range(N)]
dfs(0, 0, 0)
print(diff)