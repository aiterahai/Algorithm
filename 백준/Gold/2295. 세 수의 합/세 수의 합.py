from sys import stdin

N = int(stdin.readline())
board = [int(stdin.readline()) for i in range(N)]
left = set([i + j for i in board for j in board])
result = 0
for i in board:
    for j in board:
        if i - j in left: result = max(result, i)
print(result)