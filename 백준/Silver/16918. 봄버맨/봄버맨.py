from sys import stdin

R, C, N = map(int, stdin.readline().split())

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

board = [list(stdin.readline().rstrip()) for _ in range(R)]

if N % 2 == 0:
    print(*["O" * C for _ in range(R)], sep="\n")
    exit(0)

for _ in range(N // 2):
    bomb = [[i, j] for i in range(R) for j in range(C) if board[i][j] == "O"]
    for x, y in bomb:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
            board[nx][ny] = "O"

    board = [["O" if board[i][j] == "." else "." for j in range(C)] for i in range(R)]

for i in board:
    print(*i, sep="")