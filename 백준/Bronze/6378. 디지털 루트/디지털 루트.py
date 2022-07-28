from sys import stdin

while True:
    board = int(stdin.readline())
    if board == 0: break
    while board >= 10: board = sum(map(int, list(str(board))))
    print(board)