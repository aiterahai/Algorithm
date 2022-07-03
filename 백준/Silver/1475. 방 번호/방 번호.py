N = input()
board = [0 for i in range(10)]
for i in N: board[int(i)] += 1
board[6], board[9] = (board[6] + board[9] + 1) // 2, (board[6] + board[9] + 1) // 2
print(max(board))