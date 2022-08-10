from sys import stdin

N = int(stdin.readline())
board = list(map(int, stdin.readline().split()))
up, down = [1], [1]
for i in range(1, N): up.append(max([1] + [up[j] + 1 for j in range(len(up)) if board[i] > board[j]]))
board.reverse()
for i in range(1, N): down.append(max([1] + [down[j] + 1 for j in range(len(down)) if board[i] > board[j]]))
result = 0
for i in range(N):
    result = max(result, up[i] + down[N - i - 1])
print(result - 1)