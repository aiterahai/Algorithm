from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    Q = deque([[0, 0]])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if not maps[nx][ny] or visited[nx][ny]: continue
            Q.append([nx, ny])
            visited[nx][ny] = visited[x][y] + 1
    
    return visited[-1][-1] if visited[-1][-1] else -1