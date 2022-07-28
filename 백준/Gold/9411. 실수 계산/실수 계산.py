from sys import stdin
from decimal import Decimal, getcontext
getcontext().prec = 30
for _ in range(int(stdin.readline())):
    board = []
    while True:
        board.append(Decimal(stdin.readline()))
        if not board[-1]: break
    print(str(sum(board)).rstrip("0").rstrip("."))