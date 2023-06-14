from sys import stdin

N = int(stdin.readline())
board = list(map(int, stdin.readline().split()))
result = [0 for _ in range(1000001)]
visit = [False for _ in range(1000001)]
for index in board: visit[index] = True

for i in sorted(board):
    for j in range(i * 2, 1000001, i):
        if visit[j]: result[i], result[j] = result[i] + 1, result[j] - 1

print(*[result[index] for index in board])