from sys import stdin

for _ in range(int(stdin.readline())):
    stdin.readline()
    board = list(map(int, stdin.readline().split()))
    print(min(board), max(board))