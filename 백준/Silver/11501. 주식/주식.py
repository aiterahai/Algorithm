from sys import stdin

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    board = list(map(int, stdin.readline().split()))
    max = board[-1]
    result = 0
    for i in range(N - 2, -1, -1):
        if board[i] > max: max = board[i]
        else: result += max - board[i]
    print(result)