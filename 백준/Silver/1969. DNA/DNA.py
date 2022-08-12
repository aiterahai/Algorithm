from sys import stdin
from collections import Counter

N, M = map(int, stdin.readline().split())
board = [stdin.readline().rstrip() for _ in range(N)]
result = "".join(([sorted(list(zip(Counter([board[j][i] for j in range(N)]).keys(), Counter([board[j][i] for j in range(N)]).values())), key=lambda x:(-x[1], x[0]))[0][0] for i in range(M)]))
print(result)
print(sum(1 for i in range(N) for j in range(M) if board[i][j] != result[j]))