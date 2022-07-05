from sys import stdin

for i in range(int(stdin.readline())):
    board = stdin.readline().split()
    for j in range(len(board)): board[j] = board[j][::-1]
    print(" ".join(map(str, board)))