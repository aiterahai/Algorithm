"""
file name: 14500.py

create time: 2023-04-06 21:25
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

shape = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],

    [[0, 0], [0, 1], [1, 0], [1, 1]],

    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 1], [1, 1], [2, 1], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[1, 0], [1, 1], [1, 2], [0, 2]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],

    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 1], [0, 2], [1, 0], [1, 1]],
    [[0, 1], [1, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],

    [[1, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
    [[0, 1], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 1]]
]

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        for k in shape:
            count = 0
            for x, y in k:
                nx, ny = i + x, j + y
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    count = 0
                    break
                count += board[nx][ny]
            result = max(result, count)

print(result)