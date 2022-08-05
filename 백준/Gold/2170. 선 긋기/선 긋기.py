from sys import stdin

N = int(stdin.readline())
board = sorted([list(map(int, stdin.readline().split())) for i in range(N)])
result, left, right = 0, *board[0]
for i in range(1, N):
    if board[i][0] > right: result, left, right = result + right - left, *board[i]
    else: right = max(board[i][1], right)
print(result + right - left)