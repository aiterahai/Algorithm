from collections import deque

def solution(n, vertex):
    board = [[] for _ in range(n + 1)]
    for i, j in vertex:
        board[i].append(j)
        board[j].append(i)
    visit = [0] * (n + 1)
    visit[1] = 1
    Q = deque([1])
    while Q:
        x = Q.popleft()
        for i in board[x]:
            if visit[i]: continue
            Q.append(i)
            visit[i] = visit[x] + 1
    return visit.count(max(visit))