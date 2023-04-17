"""
file name: 2623.py

create time: 2023-04-17 23:28
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

inDegree = [0 for _ in range(N + 1)]
board = [[] for _ in range(N + 1)]

for _ in range(M):
    lines = list(map(int, stdin.readline().split()))[1:][::-1]
    while len(lines) >= 2:
        board[lines[-1]].append(lines[-2])
        inDegree[lines[-2]] += 1
        lines.pop()

Q = deque([i for i in range(1, N + 1) if not inDegree[i]])

answer = []
while Q:
    node = Q.popleft()
    answer.append(node)
    for i in board[node]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            Q.append(i)

if len(answer) != N: print(0)
else: print(*answer, sep="\n")