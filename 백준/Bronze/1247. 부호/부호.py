from sys import stdin

for _ in range(3):
    board = sum([int(stdin.readline()) for i in range(int(stdin.readline()))])
    print(0 if board == 0 else ("-" if board < 0 else "+"))