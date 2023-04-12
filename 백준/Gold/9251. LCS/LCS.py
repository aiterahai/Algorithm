"""
file name: 9251.py

create time: 2023-04-12 11:30
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()
table = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]: table[i][j] = table[i - 1][j - 1] + 1
        else: table[i][j] = max(table[i - 1][j], table[i][j - 1])

print(table[-1][-1])