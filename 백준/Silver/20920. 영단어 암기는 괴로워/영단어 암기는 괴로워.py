from sys import stdin
from collections import Counter

N, M = map(int, stdin.readline().split())
board = Counter([word for word in [stdin.readline().rstrip() for _ in range(N)] if len(word) >= M])
print(*sorted(board.keys(), key=lambda x: (-board[x], -len(x), x)), sep="\n")
