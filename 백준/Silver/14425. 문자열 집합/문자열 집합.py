from sys import stdin
from collections import Counter

N, M = map(int, stdin.readline().split())
board = [stdin.readline().strip() for i in range(N)]
answer = Counter([stdin.readline().strip() for i in range(M)])
count = 0
for i in board:
    try:
        count += answer[i]
    except:
        pass
print(count)