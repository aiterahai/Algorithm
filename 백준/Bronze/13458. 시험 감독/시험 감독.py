from sys import stdin

N = int(stdin.readline())
board = list(map(int, stdin.readline().split()))
B, C = map(int, stdin.readline().split())

print(sum([max((i - B - 1) // C + 1, 0) for i in board]) + N)