def solution(N):
    answer = []
    board = [[0 for i in range(N)] for j in range(N)]
    x, y, d = 0, 0, 0
    dx, dy = [1, 0, -1], [0, 1, -1]
    for cnt in range(1, (1+N)*N//2 + 1):
        board[x][y] = cnt
        x, y = x + dx[d], y + dy[d]
        if x >= N or y >= N or board[x][y]:
            x, y = x - dx[d], y - dy[d]
            d = (d + 1) % 3
            x, y = x + dx[d], y + dy[d]
    for i in board:
        for j in i:
            if j: answer.append(j)
    return answer