from sys import stdin

N = int(stdin.readline())
inp = stdin.readline().rstrip()
board = []
for i in inp:
    if board and i == board[-1]: continue
    board.append(i)
board = "".join(board)
print(min(board.count("B"), board.count("R")) + 1)