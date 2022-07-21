from sys import stdin

while True:
    board = stdin.readline()[:-1]
    if not board: break
    result = [0, 0, 0, 0]
    for i in board:
        if i.islower(): result[0] += 1
        elif i.isupper(): result[1] += 1
        elif i.isdigit(): result[2] += 1
        elif i.isspace(): result[3] += 1

    print(*result)