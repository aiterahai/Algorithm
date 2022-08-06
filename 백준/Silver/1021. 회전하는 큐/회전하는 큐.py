from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().split())
board = list(map(int, stdin.readline().split()))[::-1]
Q = deque([i for i in range(1, N + 1)])
count = 0
while board:
    idx = board.pop()
    if Q.index(idx) <= len(Q) // 2:
        while Q[0] != idx:
            count += 1
            Q.append(Q.popleft())
        Q.popleft()
    else:
        while Q[0] != idx:
            count += 1
            Q.appendleft(Q.pop())
        Q.popleft()
print(count)