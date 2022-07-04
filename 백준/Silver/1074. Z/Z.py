board = [0] + [2 ** i for i in range(50)]
def func(N, r, c, x, y, count):
    if not N: return count
    if r <= x and c <= y: return func(N - 1, r, c, x - board[N - 1], y - board[N - 1], count)
    elif r > x and c > y: return func(N - 1, r, c, x + board[N - 1], y + board[N - 1], count + 3 * board[2*N-1])
    elif r <= x and c > y: return func(N - 1, r, c, x - board[N - 1], y + board[N - 1], count + board[2 * N - 1])
    else: return func(N - 1, r, c, x + board[N - 1], y - board[N - 1], count + 2 * board[2*N-1])

N, r, c = map(int, input().split())
print(func(N, r + 1, c + 1, board[N], board[N], 0))