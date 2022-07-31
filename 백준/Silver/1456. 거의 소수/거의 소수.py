from sys import stdin

A, B = map(int, stdin.readline().split())
board = [True] * (int(B ** 0.5) + 1)
board[0], board[1] = False, False
for i in range(2, int(B ** 0.5) + 1):
    if not board[i]: continue
    for j in range(i ** 2, int(B ** 0.5) + 1, i):
        board[j] = False
prime = [i for i in range(len(board)) if board[i]]
result = 0
for i in prime:
    if i ** 2 > B: break
    for j in range(2, 100000):
        if A <= i ** j:
            if i ** j <= B: result += 1
            else: break
print(result)