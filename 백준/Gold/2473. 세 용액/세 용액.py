"""
file name: 2473.py

create time: 2023-04-18 09:26
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

N = int(stdin.readline())
board = sorted(list(map(int, stdin.readline().split())))
result = int(1e15)
solution = []

for i in range(N):
    cur = board[i]
    start, end = 0, N - 1
    while end > start:
        if start == i: start += 1
        if end == i: end -= 1
        if start == end: break
        value = cur + board[start] + board[end]
        if result > abs(value):
            result = abs(value)
            solution = [board[i], board[start], board[end]]
        if value < 0: start += 1
        else: end -= 1

print(*solution)