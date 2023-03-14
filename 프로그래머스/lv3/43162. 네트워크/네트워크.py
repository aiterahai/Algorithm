from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if visited[i]: continue
        Q = deque([i])
        while Q:
            x = Q.popleft()
            visited[x] = True
            for j in range(n):
                if not computers[x][j] or visited[j]: continue
                Q.append(j)
        answer += 1
    return answer