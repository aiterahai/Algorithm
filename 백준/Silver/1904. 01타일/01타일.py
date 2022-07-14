N = int(input())
board = [1, 2]
for i in range(N-1): board[i % 2] = sum(board) % 15746
print(board[(N + 1) % 2])