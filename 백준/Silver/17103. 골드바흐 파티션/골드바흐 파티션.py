from sys import stdin

board = [True] * 1000001
board[0], board[1] = False, False
for i in range(2, int(1000001 ** 0.5) + 1):
    if not board[i]: continue
    for j in range(i ** 2, 1000001, i):
        board[j] = False

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    result = 0
    for i in range(2, N // 2 + 1):
        if board[i] and board[N - i]:
            result += 1
    print(result)