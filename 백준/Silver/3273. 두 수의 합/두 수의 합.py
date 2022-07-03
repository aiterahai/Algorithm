N = int(input())
board = sorted(list(map(int, input().split())))
X = int(input())
start, end = 0, len(board)-1
count = 0
while end > start:
    if board[start] + board[end] < X: start += 1
    elif board[start] + board[end] > X: end -= 1
    else: count, start, end = count + 1, start + 1, end - 1
print(count)