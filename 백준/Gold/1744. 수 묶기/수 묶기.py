from sys import stdin
from collections import deque

N = int(stdin.readline())
board = deque(sorted([int(stdin.readline()) for _ in range(N)]))
result = 0
while len(board) >= 2:
    if board[-1] * board[-2] > board[0] * board[1] and board[-1] * board[-2] >= board[-1] + board[-2]:
        result += board.pop() * board.pop()
    elif board[0] * board[1] >= board[0] + board[1]:
        result += board.popleft() * board.popleft()
    else: result += board.popleft() + board.popleft()
print(result + sum(board))