from sys import stdin
from collections import deque
N = int(stdin.readline())
board = deque(sorted(list(map(int, stdin.readline().split()))))
M = board.pop() if N % 2 else int(1e9)
while board: M = max(M, board.pop() + board.popleft())
print(M)