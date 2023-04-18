"""
file name: 10942.py

create time: 2023-04-17 19:13
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

N = int(stdin.readline())
board = list(map(int, stdin.readline().split()))
table = [[0 for _ in range(N)] for _ in range(N)]

for length in range(N):
    for s in range(N - length):
        e = s + length

        if s == e: table[s][e] = 1
        elif board[s] == board[e]:
            if s + 1 == e: table[s][e] = 1
            else: table[s][e] = table[s + 1][e - 1]

for _ in range(int(stdin.readline())):
    s, e = map(int, stdin.readline().split())
    print(table[s - 1][e - 1])