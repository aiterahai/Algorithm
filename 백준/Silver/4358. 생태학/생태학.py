from collections import Counter
from sys import stdin

board = []
count = -1
while True:
    board.append(stdin.readline().rstrip())
    count += 1
    if not board[-1]: break
board.pop()
C = Counter(board)
board = []
for i in C.keys(): board.append([i, C[i] / count * 100])
for i, j in sorted(board, key=lambda x:(x[0])): print(f"{i} {j:.4f}")