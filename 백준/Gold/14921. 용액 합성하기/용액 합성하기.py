from sys import stdin

N = int(stdin.readline())
board = sorted(list(map(int, stdin.readline().split())))
result = [1000000000, 1000000000]
start, end = 0, N - 1
while start < end:
    temp = board[start] + board[end]
    if abs(temp) < abs(sum(result)): result = [board[start], board[end]]
    if temp < 0: start += 1
    else: end -= 1
print(sum(result))