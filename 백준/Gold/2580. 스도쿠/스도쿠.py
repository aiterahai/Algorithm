from sys import stdin

def check(x, y, value):
    for i in range(9):
        if board[x][i] == value: return True
        if board[i][y] == value: return True
    for i in range(x - x % 3, x - x % 3 + 3):
        for j in range(y - y % 3, y - y % 3 + 3):
            if board[i][j] == value: return True
    return False

def dfs(K):
    if K == N:
        for i in board: print(*i)
        exit(0)
    x, y = index[K]
    for i in range(1, 10):
        if check(x, y, i): continue
        board[x][y] = i
        dfs(K + 1)
        board[x][y] = 0


board = [list(map(int, stdin.readline().split())) for i in range(9)]
index = [[i, j] for i in range(9) for j in range(9) if not board[i][j]]
N = len(index)
dfs(0)