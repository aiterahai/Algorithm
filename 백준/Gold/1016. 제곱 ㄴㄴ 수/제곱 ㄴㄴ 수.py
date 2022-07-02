from math import sqrt

A, B = map(int, input().split())
board = set()
for i in range(2, int(sqrt(B)) + 1):
    for j in range(int(A/i**2), int(B/i**2) + 1):
        temp = (i ** 2) * j
        if A <= temp <= B: board.add(temp)
print(B - A + 1 - len(board))