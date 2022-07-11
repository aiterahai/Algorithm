from sys import stdin

N, S = map(int, stdin.readline().split())
board = list(map(int, stdin.readline().split()))

start, end, result, total = 0, 0, 9999999, 0
while True:
    try:
        if total >= S:
            result = min(result, abs(end - start))
            total = total - board[start]
            start += 1
        else:
            total = total + board[end]
            end += 1
    except: break
if result == 9999999: print(0)
else: print(result)