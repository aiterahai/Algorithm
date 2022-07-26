from sys import stdin

answer = int(1e10)
visit = []
def count():
    global answer
    A, B = 1, 0
    for i in range(len(visit)):
        if not visit[i]: continue
        A *= board[i][0]
        B += board[i][1]
    if A == 1 and B == 0: return
    answer = min(answer, abs(A-B))
def dfs():
    if len(visit) == N: count(); return
    for i in range(2):
        visit.append(i)
        dfs()
        visit.pop()
N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for i in range(N)]
dfs()
print(answer)