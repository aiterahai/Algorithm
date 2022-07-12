board = [0, 1]
for i in range(89): board.append(board[-1] + board[-2])
print(board[int(input())])