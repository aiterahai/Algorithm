from sys import stdin

N = int(stdin.readline())
A, B, C, D = zip(*[list(map(int, stdin.readline().split())) for _ in range(N)])
board = {}
for i in A:
    for j in B:
        board[i + j] = board.get(i + j, 0) + 1

result = 0
for i in C:
    for j in D:
        result += board.get(-i - j, 0)
print(result)