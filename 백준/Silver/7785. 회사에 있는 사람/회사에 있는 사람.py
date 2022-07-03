from sys import stdin

T = int(stdin.readline())
board = set()
for i in range(T):
    log = stdin.readline().split()
    if log[1] == "enter": board.add(log[0])
    else: board.remove(log[0])
for i in sorted(board, reverse=True): print(i)