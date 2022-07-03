board = [i for i in range(1, 21)]
for i in range(10):
    a, b = map(int, input().split())
    board = board[:a-1] + board[b-1:a-1:-1] + board[a-1:a] + board[b:]
print(" ".join(map(str, board)))