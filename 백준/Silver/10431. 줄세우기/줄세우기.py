from sys import stdin

for _ in range(int(stdin.readline())):
    value = list(map(int, stdin.readline().split()))
    T, board = value[0], value[1:]
    result = 0
    for i in range(1, 20):
        for j in range(i):
            if board[i] < board[j]: result += 1
    print(T, result)