from sys import stdin
from collections import deque

N = int(stdin.readline())
board = sorted([int(stdin.readline()) for i in range(N)])
answer = 0
while len(board) >= 3:
    answer += board.pop() + board.pop()
    board.pop()
print(answer + sum(board))