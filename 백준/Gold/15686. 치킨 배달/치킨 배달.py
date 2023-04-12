"""
file name: 15686.py

create time: 2023-04-10 09:17
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
chicken = [[i, j] for i in range(N) for j in range(N) if board[i][j] == 2]
house = [[i, j] for i in range(N) for j in range(N) if board[i][j] == 1]
result = min([sum([min([abs(x - nx) + abs(y - ny) for nx, ny in store]) for x, y in house]) for store in list(combinations(chicken, M))])
print(result)