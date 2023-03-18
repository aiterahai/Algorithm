from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    dx, dy = [0, 1, 0 ,-1], [1, 0 ,-1, 0]
    start = find(maps, "S") + find(maps, "L")
    end = [start[-1]] + find(maps, "E")
    answer = []
    Q = deque()
    for k in range(2):
        visit = [[0 for _ in range(M)] for _ in range(N)]
        Q.append(start[k])
        visit[start[k][0]][start[k][1]] = 1
        while Q:
            x, y = Q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                if maps[nx][ny] == "X" or visit[nx][ny]: continue
                visit[nx][ny] = visit[x][y] + 1
                Q.append([nx, ny])
        answer.append(visit[end[k][0]][end[k][1]])
    return -1 if answer[0] == 0 or answer[1] == 0 else sum(answer) - 2

def find(maps, value):
    N, M = len(maps), len(maps[0])
    return [[i, j] for j in range(M) for i in range(N) if maps[i][j] == value]