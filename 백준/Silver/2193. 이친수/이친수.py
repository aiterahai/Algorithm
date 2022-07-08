N = int(input())
board = [0 for i in range(91)]
board[1], board[2] = 1, 1
for i in range(3, 91): board[i] = board[i - 1] + board[i - 2]
print(board[N])