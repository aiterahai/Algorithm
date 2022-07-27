from sys import stdin

N = int(stdin.readline())
board = sorted([int(stdin.readline()) for i in range(N)])
answer = 0
while board: answer = answer + max(board.pop() - N + len(board) + 1, 0)
print(answer)