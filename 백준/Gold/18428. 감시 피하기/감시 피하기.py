from sys import stdin
from itertools import combinations

N = int(stdin.readline())
board = [list(stdin.readline().split()) for _ in range(N)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

obstacles = list(combinations([(x, y) for x in range(N) for y in range(N) if board[x][y] == "X"], 3))
teachers = [(x, y) for x in range(N) for y in range(N) if board[x][y] == "T"]

for obstacle in obstacles:
    for x, y in obstacle: board[x][y] = "O"

    breaks = False
    count = 0
    for x, y in teachers:
        for i in range(4):
            nx, ny = x, y
            while True:
                nx, ny = nx + dx[i], ny + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N: break
                if board[nx][ny] == "O": break
                if board[nx][ny] == "S":
                    breaks = True
                    count += 1
                    break
            if breaks: break
        if breaks: break

    if count == 0:
        print("YES")
        exit(0)

    for x, y in obstacle: board[x][y] = "X"

print("NO")