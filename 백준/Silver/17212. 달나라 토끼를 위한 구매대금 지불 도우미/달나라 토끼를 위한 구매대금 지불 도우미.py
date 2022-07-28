from sys import stdin

N = int(stdin.readline())
board = [N % 7 % 5 % 2, N % 7 % 5 // 2, N % 7 // 5, N // 7]
while board[0] > 0 and board[1] > 0 and board[3] > 0: board[0], board[1], board[2], board[3] = board[0] - 1, board[1] - 1, board[2] + 2, board[3] - 1
print(sum(board))