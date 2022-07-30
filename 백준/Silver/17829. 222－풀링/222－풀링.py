from sys import stdin

def func(x, y, N):
    if N == 2: return sorted([board[x][y], board[x+1][y], board[x][y+1], board[x+1][y+1]])[-2]
    return sorted([func(x, y, N // 2), func(x + N // 2, y, N // 2), func(x, y + N // 2, N // 2), func(x + N // 2, y + N // 2, N // 2)])[-2]
N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for i in range(N)]
print(func(0, 0, N))