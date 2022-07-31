from sys import stdin

board = [True] * 100001
board[0], board[1] = False, False
for i in range(2, int(100001 ** 0.5) + 1):
    if not board[i]: continue
    for j in range(i ** 2, int(100001 ** 0.5) + 1, i):
        board[j] = False

prime = [i for i in range(100001) if board[i]]

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    index = 0
    while N != 1:
        count = 0
        while N % prime[index] == 0:
            N = N // prime[index]
            count += 1
        if count: print(f"{prime[index]} {count}")
        index += 1