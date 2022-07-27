from sys import stdin

N, K = map(int, stdin.readline().split())
board = list(map(int, stdin.readline().split()))
print(sum(sorted([board[i] - board[i-1] for i in range(1, N)])[:N-K]))