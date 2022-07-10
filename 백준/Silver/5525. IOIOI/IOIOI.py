from sys import stdin
N = int(stdin.readline())
M = int(stdin.readline())
board = stdin.readline().rstrip()

result, count, i = 0, 0, 1
while i < M - 1:
    if board[i - 1] == "I" and board[i] == "O" and board[i + 1] == "I": count, i = count + 1, i + 1
    else: count = 0
    if count == N: count, result = count - 1, result + 1
    i += 1
print(result)