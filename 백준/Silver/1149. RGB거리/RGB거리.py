from sys import stdin

N = int(stdin.readline())
RGB = [list(map(int, stdin.readline().split())) for _ in range(N)]
board = [[0, 0, 0] for _ in range(N)]
board[0] = [RGB[0][0], RGB[0][1], RGB[0][2]]
for i in range(1, N):
    board[i][0] = RGB[i][0] + min(board[i - 1][1], board[i - 1][2])
    board[i][1] = RGB[i][1] + min(board[i - 1][0], board[i - 1][2])
    board[i][2] = RGB[i][2] + min(board[i - 1][0], board[i - 1][1])
print(min(board[N-1]))