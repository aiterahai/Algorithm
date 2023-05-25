from sys import stdin

board = set()
board.add("ChongChong")
for _ in range(int(stdin.readline())):
    A, B = stdin.readline().split()
    if A in board or B in board:
        board.add(A)
        board.add(B)
print(len(board))