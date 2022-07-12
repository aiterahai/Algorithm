N, M = map(int, input().split())
board = list(map(int, input().split()))
start, end = 0, 0
total = 0
count = 0
while True:
    try:
        if total < M:
            total += board[end]
            end += 1
        elif total > M:
            total -= board[start]
            start += 1
        else:
            count += 1
            total = total + board[end] - board[start]
            start, end = start + 1, end + 1
    except: break
print(count)