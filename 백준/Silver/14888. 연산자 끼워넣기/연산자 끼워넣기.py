from sys import stdin
N = int(stdin.readline())
board = list(map(int, stdin.readline().split()))
operator = list(map(int, stdin.readline().split()))
visit = []
m, M = int(1e9), -int(1e9)
def result():
    global m, M
    answer = board[0]
    for i in range(N - 1):
        if visit[i] == "//" and answer < 0: answer = eval(f"-({-answer}{visit[i]}{board[i+1]})")
        else: answer = eval(f"{answer}{visit[i]}{board[i+1]}")
    m, M = min(answer, m), max(answer, M)
def dfs(K):
    if K == N: result(); return
    for i, op in enumerate(["+", "-", "*", "//"]):
        if operator[i] <= 0: continue
        operator[i] -= 1; visit.append(op)
        dfs(K + 1)
        operator[i] += 1; visit.pop()
dfs(1)
print(f"{M}\n{m}")